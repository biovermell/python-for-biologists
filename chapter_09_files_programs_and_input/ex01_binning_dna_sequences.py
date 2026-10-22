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

# 1. FOLDER CREATION
os.mkdir("./dna_bins/")
for number in range(100, 1000, 100):
    bin_name = f"{number}-{number + 99}"
    os.makedirs(os.path.join("./dna_bins", bin_name))


# 2. DNA BINNING
def dna_binning(length):
    bin = length // 100 * 100
    folder_name = f"{bin}-{bin + 99}"
    return folder_name


# 3. I/O
# To name the new files
seq_number = 1
for file in os.listdir("./dna_seqs"):
    file_path = "./dna_seqs/" + file
    with open(file_path, "r") as infile:
        for line in infile:
            seq = line.strip().upper()
            length = len(seq)
            folder_name = dna_binning(length)
            with open(f"./dna_bins/{folder_name}/seq_{seq_number}.dna", "w") as outfile:
                outfile.write(seq)
            seq_number += 1
