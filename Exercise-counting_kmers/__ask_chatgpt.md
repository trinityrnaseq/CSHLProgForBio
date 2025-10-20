

# Initial specification to ChatGPT


- Prompt:


We want to write a python program that counts kmers from reads in a fastq file.
The input to the script should be the name of the target fastq file and the kmer size.
The kmers should overlap along each sequence by size k-1, shifting the kmer window by each base along each sequence.
The output should include two columns including the kmer sequence and the count and shown in descending order according to the count value.
Let's include an option to limit the output to some specified top number of most abundant kmers.


# Extension - incorporate entropy value

- Prompt: 
Can we include an additional column that includes the Shannon's entropy value for that kmer?

>If you notice anything peculiar in the output when running the code, show the results to chatgpt and ask to explain it.


# Extension - build an inchworm assembler

- Prompt:
    
Now that we have a kmer count dictionary, can we build a Trinity Inchworm like assembler that will perform contig extensions from the dominant kmer as a seed and require the seed to have a minimum entropy value?


- Things to contemplate as part of your conversation, code evolution, and testing:

    - Does it run at all?
    - Does it report anything? If not, could it be in an infinite loop somehow?
    - Might it incorporate some logging information so you can better monitor its progress?
    - If it generates contigs, do they appear biological? (try blastn at NCBI)
    - Is the k-mer size used too small? Try k = 25 like in the official inchworm
    - Are there other constraints we might include for the output?




