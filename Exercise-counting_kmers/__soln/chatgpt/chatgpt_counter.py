#!/usr/bin/env python3
import argparse
from collections import Counter
import gzip


def read_fastq_sequences(fastq_file):
    """Yield sequences from a FASTQ or FASTQ.GZ file."""
    open_func = gzip.open if fastq_file.endswith(".gz") else open
    with open_func(fastq_file, "rt") as fh:
        while True:
            header = fh.readline()
            if not header:
                break
            seq = fh.readline().strip()
            fh.readline()  # plus line
            fh.readline()  # quality line
            yield seq


def count_kmers(fastq_file, k):
    """Count all kmers of length k from FASTQ reads."""
    kmer_counts = Counter()
    for seq in read_fastq_sequences(fastq_file):
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i : i + k]
            kmer_counts[kmer] += 1
    return kmer_counts


def main():
    parser = argparse.ArgumentParser(description="Count k-mers from a FASTQ file.")
    parser.add_argument("fastq", help="Input FASTQ file (can be .gz)")
    parser.add_argument("k", type=int, help="k-mer size")
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="Limit output to the top N most abundant kmers",
    )
    args = parser.parse_args()

    counts = count_kmers(args.fastq, args.k)
    # Sort by count descending, then kmer lexicographically
    sorted_kmers = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    if args.top:
        sorted_kmers = sorted_kmers[: args.top]

    # Print header and results
    print("kmer\tcount")
    for kmer, count in sorted_kmers:
        print(f"{kmer}\t{count}")


if __name__ == "__main__":
    main()
