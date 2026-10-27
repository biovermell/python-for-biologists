"""
Chapter 09, exercise 02: Kmer counting
Write a program that will calculate the number of all kmers
of a given length across all DNA sequences in the input files
and display just the ones that occur more than a given number
of times.
You program should take two command line arguments –
the kmer length, and the cutoff number.
"""

# 0. PREAMBLE
import os
import sys

# 1. COMMAND LINE ARGUMENTS
length = int(sys.argv[1])
cutoff = int(sys.argv[2])


# N. KMER MAKING
def kmer_maker(seq, length):
    kmers = []
    for number in range(0, len(seq) - (length - 1), 1):
        kmer = seq[number : number + length]
        kmers.append(kmer)
        return kmers


# N. FILE READING
for file in os.listdir("./dna_seqs"):
    file_path = "./dna_seqs/" + file
    with open(file_path, "r") as infile:
        for line in infile:
            seq = line.strip().upper()

# N. OUTPUT PRINTING
