#!/bin/bash

set -ex

./fastq_file_to_sequence_list.py ../reads.fq 10

./sequence_to_kmer_list.py ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT 6

./count_kmers_from_fastq.py ../reads.fq 8 10

./count_kmers_from_fastq.with_entropy.py ../reads.fq 8 10
