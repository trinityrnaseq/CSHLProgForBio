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

>Hint: if reading the fastq file line by line, you can use a line counter to determine which position you are at in each fastq record. By using the modulus operator (%) with the line counter, you can readily determine your position within each record. For exmaple, compare the line count and (line_count % 4) to see how they vary.


## Part B: Extracting kmers from a sequence

Write a python script to extract all kmers of a specified length from a nucleotide sequence.

A script [sequence_to_kmer_list.py](sequence_to_kmer_list.py) is provided as a starting point.  Fill in the missing code.

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


>Hint: Picture sliding a window of size kmer_length across the sequence mvoing one base at a time.

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

>Hint: for sorting a list of features (ex. kmers) based on attributes (eg. abundance), examine the 'key' parameter of the 'sorted' method along with a lambda.


## Extra credit section:

If you've accomplished the above, here's another challenge!

Note that the top-most kmer is of low complexity.  If we are going to perform downstram operations like assembly and want to start with a seed kmer, we might want to avoid low complexity kmers as they would lack specificity.

Challenge:  include another method that computes the complexity of each kmer using Shannon's Entropy
      (example:  see: https://en.wikipedia.org/wiki/Sequence_logo#Logo_creation ), and picture the kmer as representing one column of the seqlogo for which you would get one entropy calculation.

Add the entropy value as another column in the above printing.

    
