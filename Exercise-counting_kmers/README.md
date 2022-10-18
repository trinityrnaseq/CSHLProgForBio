# Counting k-mers

We're going to write a python program that counts kmers from reads in a fastq file.  To do this, we'll first break the task up into smaller parts involving:

* A. retrieving the sequences from the fastq file
* B. extracting kmers from a sequence
* C. counting the kmers among all sequences

Let's tackle each in the above order, and in the process, be generating a library of reusable python methods.



## Part A: Retrieve sequences from a fastq file

Write a python script that retrieves a list of all read sequences from a fastq file. 

A script [fastq_file_to_sequence_list.py](fastq_file_to_sequence_list.py) is provided as a starting point.  Fill in the missing code.

A fastq file <reads.fq> is provided as input.

The script usage is:

```
    usage: ./fastq_file_to_sequence_list.py filename.fastq num_seqs_show
```

Running it like so:

```
    fastq_file_to_sequence_list.py reads.fq 10
```

Should produce the following output:

['ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT', 'GTAATTTCCGTACCTGCCACAGTGTGGGCTCACCCTGCTTAGAGGACAGGGAAGGACCCTAAAGGTAGGCTGATGC', 'CTGGGCTGCAGCTAAGTTCTCTGCATCCTCCTTCTTGCTTGTGGCTGGGAAGAAGACAATGTTGTCGATGGTCTGG', 'CACGTTTTCTAAGCAGTTTGTACCAGATCGTGCTAACTGCTCATTGTCTTGTTGTACACACCAGTAAAGCTGGGCA', 'TGCTCATTGTCTTGTTGTACACACCAGTAAAGCTGGGCAAAAATATCATCCAAAAGTACATCGCTGAGAACTCCTA', 'CCCACCTGAAAACATTTTCTACATCCACTGTTATATGGAATGCTTGATAAGCTTTTCATTCTAACCATCAGAGCAC', 'TCTGAATAAGTCCTGCCACCAATGTTTTTCATAAGTGTGGCCATATGTTTTCATTATTTCAAACATTACTGTTAAG', 'CTCCGTTTTTTGAGAGTGCAACACATAGATACTGCTTGATAGCATTAATAAACATCTCATTTGTCCTGAAAACAGG', 'GCCTGAGTGTGCAAAAATCTTCAGAGTAAGAATACCATAGTTGCTAAATATCTTTTACCATGAGCAATAATTTTTT', 'TCTGGTGCAGCTAGATGGAATACTGAGAAAATGTTCTTCCATCCTGAACGAATATTTGCAGCCTGAGAATTAACCA']


## Part B: Extracting kmers from a sequence

Write a python script to extract all kmers of a specified length from a nucleotide sequence.

A script [fastq_file_to_sequence_list.py](fastq_file_to_sequence_list.py) is provided as a starting point.  Fill in the missing code.

The script usage is:

```
   usage: ./sequence_to_kmer_list.py sequence kmer_length
```

Running it like so:

```
    sequence_to_kmer_list.py ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT 6
```

Should produce the following output:

['ACTGCA', 'CTGCAT', 'TGCATC', 'GCATCC', 'CATCCT', 'ATCCTG', 'TCCTGG', 'CCTGGA', 'CTGGAA', 'TGGAAA', 'GGAAAG', 'GAAAGA', 'AAAGAA', 'AAGAAT', 'AGAATC', 'GAATCA', 'AATCAA', 'ATCAAT', 'TCAATG', 'CAATGG', 'AATGGT', 'ATGGTG', 'TGGTGG', 'GGTGGC', 'GTGGCC', 'TGGCCG', 'GGCCGG', 'GCCGGA', 'CCGGAA', 'CGGAAA', 'GGAAAG', 'GAAAGT', 'AAAGTG', 'AAGTGT', 'AGTGTT', 'GTGTTT', 'TGTTTT', 'GTTTTT', 'TTTTTC', 'TTTTCA', 'TTTCAA', 'TTCAAA', 'TCAAAT', 'CAAATA', 'AAATAC', 'AATACA', 'ATACAA', 'TACAAG', 'ACAAGA', 'CAAGAG', 'AAGAGT', 'AGAGTG', 'GAGTGA', 'AGTGAC', 'GTGACA', 'TGACAA', 'GACAAT', 'ACAATG', 'CAATGT', 'AATGTG', 'ATGTGC', 'TGTGCC', 'GTGCCC', 'TGCCCT', 'GCCCTG', 'CCCTGT', 'CCTGTT', 'CTGTTG', 'TGTTGT', 'GTTGTT', 'TTGTTT']


## Part C: Counting all kmers from all sequences in a fastq file

Now, let's count all kmers in all sequences.  We can leverage each of the methods implemented above. Because of the way we wrote the above scripts, we can leverage them as a code library and simply import them for use in a new script.

Use the script [count_kmers_from_fastq.py](count_kmers_from_fastq.py) as the starting point.  You'll see at the top of this script:

```
from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *
```

Those lines import the methods we implemented earlier so that we can just reuse them without having to rewrite or copy/paste any code in this new script.

The usage of our script is:

```
    usage: ./count_kmers_from_fastq.py filename.fastq kmer_length num_top_kmers_show
```

And when we run it like so:

```
    count_kmers_from_fastq.py reads.fq 6 10
```

It should produce the output:

```
TTTTTT: 3085
CTTCTT: 2550
AAAAAA: 2498
CTGCTG: 2446
AGCTGG: 2400
CAGCAG: 2265
CAGCTG: 2243
TCTTCT: 2208
CTGGAG: 2174
TGCTGT: 2156
```

