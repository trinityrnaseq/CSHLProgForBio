#!/usr/bin/env python3
import argparse
from collections import Counter
import math
import sys
import time


def shannon_entropy(seq):
    """Compute Shannon entropy for a DNA sequence."""
    freq = Counter(seq)
    total = len(seq)
    probs = [count / total for count in freq.values()]
    entropy = -sum(p * math.log2(p) for p in probs)
    return 0.0 if abs(entropy) < 1e-12 else entropy


def extend_contig(seed, kmer_counts, k):
    """Greedily extend contig left and right from a seed k-mer."""
    contig = seed
    used = set([seed])

    # --- Extend to the right ---
    while True:
        suffix = contig[-(k - 1) :]
        candidates = [(suffix + b) for b in "ACGT"]
        valid = [
            (c, kmer_counts[c])
            for c in candidates
            if c in kmer_counts and c not in used
        ]
        if not valid:
            break
        best, _ = max(valid, key=lambda x: x[1])
        contig += best[-1]
        used.add(best)

    # --- Extend to the left ---
    while True:
        prefix = contig[: k - 1]
        candidates = [(b + prefix) for b in "ACGT"]
        valid = [
            (c, kmer_counts[c])
            for c in candidates
            if c in kmer_counts and c not in used
        ]
        if not valid:
            break
        best, _ = max(valid, key=lambda x: x[1])
        contig = best[0] + contig
        used.add(best)

    return contig, used


def assemble_inchworm(kmer_counts, min_entropy=0.0, log_interval=1000):
    """Simplified Trinity Inchworm-like assembler with progress logging."""
    assembled_contigs = []
    k = len(next(iter(kmer_counts)))  # infer k-mer size
    total_kmers = len(kmer_counts)

    print(
        f"[info] Starting Inchworm-like assembly with {total_kmers:,} kmers (k={k})",
        file=sys.stderr,
    )
    print(f"[info] Minimum seed entropy = {min_entropy}", file=sys.stderr)
    start_time = time.time()

    contig_counter = 0
    while kmer_counts:
        # choose highest-count remaining kmer
        kmer, count = max(kmer_counts.items(), key=lambda x: x[1])
        ent = shannon_entropy(kmer)

        # skip low-entropy seeds
        if ent < min_entropy:
            del kmer_counts[kmer]
            continue

        contig_counter += 1
        contig, used = extend_contig(kmer, kmer_counts, k)
        assembled_contigs.append(contig)

        # remove used kmers from pool
        for u in used:
            if u in kmer_counts:
                del kmer_counts[u]

        # logging
        if contig_counter == 1 or contig_counter % 10 == 0:
            remaining = len(kmer_counts)
            elapsed = time.time() - start_time
            print(
                f"[log] contigs={contig_counter:5d} | remaining kmers={remaining:,} | "
                f"elapsed={elapsed:6.1f}s | seed={kmer} ({count}×, H={ent:.2f})",
                file=sys.stderr,
            )

        if contig_counter % log_interval == 0:
            sys.stderr.flush()

    print(
        f"[done] Assembled {contig_counter} contigs in {time.time() - start_time:.1f}s",
        file=sys.stderr,
    )
    return assembled_contigs


def main():
    parser = argparse.ArgumentParser(
        description="Simplified Trinity Inchworm-like assembler using k-mer counts (with entropy filtering and logging)."
    )
    parser.add_argument(
        "kmer_counts_file", help="Input TSV with kmer and count columns"
    )
    parser.add_argument(
        "--min_entropy",
        type=float,
        default=0.0,
        help="Minimum Shannon entropy required for a seed k-mer",
    )
    parser.add_argument(
        "--log_interval",
        type=int,
        default=1000,
        help="How often to flush logs (number of contigs)",
    )
    args = parser.parse_args()

    # --- Load k-mer counts ---
    kmer_counts = {}
    with open(args.kmer_counts_file) as f:
        header = next(f)
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            kmer, count = parts[0], int(parts[1])
            kmer_counts[kmer] = count

    # --- Run assembler ---
    contigs = assemble_inchworm(kmer_counts, args.min_entropy, args.log_interval)

    # --- Output contigs in FASTA format ---
    for i, c in enumerate(contigs, 1):
        print(f">contig_{i}\n{c}")


if __name__ == "__main__":
    main()
