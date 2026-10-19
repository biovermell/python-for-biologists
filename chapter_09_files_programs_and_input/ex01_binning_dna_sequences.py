"""
Chapter 09, exercise 01: Binning DNA sequences
Given a a collection of files which contain DNA sequences
of varying length, write a program which creates nine
new folders – one for sequences 100-199 bases long, one
for sequences 200-299 bases long, etc.
Write out each DNA sequence in the input files to a
separate file in the appropriate folder
"""

# 0. PREAMBLE
import os

# import shutil

# 1. FOLDER CREATION
os.mkdir("./dna_bins/")
for number in range(100, 1000, 100):
    bin_name = f"{number - 99} - {number}"
    os.makedirs(f"./dna_bins/{bin_name}")

# 2. DNA BINNING
for file in os.listdir("./dna_seqs"):
    with open(file, "r") as infile:
        for line in infile:
            seq = line.strip().upper()    
            length = len(seq)

    