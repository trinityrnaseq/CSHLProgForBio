#!/usr/bin/env python

import os, sys, re
import subprocess

usage = "\n\n\tusage: {} trans_alignments.sam\n\n\n"

if len(sys.argv) < 2:
    sys.stderr.write(usage)
    sys.exit(1)


def main():

    # capture command line argument
    samfile = sys.argv[1]
    
    # create hashtable for storing reads associated with genes
    gene_read_counter = dict()

    # read the sam formatted output line by line
    for line in open(samfile):
        line = line.rstrip()

        # split line into the tab-delimited fields, grab the read and transcript ids
        fields = line.split("\t")
        read_name = fields[0]
        transcript = fields[2]

        # transcript name has format:  gene^transcript
        # capture the gene identifier
        
        (gene_name, transcript_name) = transcript.split("^")

        # increment the read count for that gene
        if gene_name in gene_read_counter:
            read_set = gene_read_counter[gene_name]
            read_set.add(read_name)
        else:
            gene_read_counter[gene_name] = set()
            gene_read_counter[gene_name].add(read_name)

    
    # generate report
    for gene_name in sorted(gene_read_counter, key=lambda x:len(gene_read_counter[x]), reverse=True):
        read_set = gene_read_counter[gene_name]
        num_reads = len(read_set)
        print("\t".join([gene_name, str(num_reads)]))
         
    sys.exit(0)
    


if __name__ == '__main__':
    main()
