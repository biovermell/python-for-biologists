"""
Given DNA sequences from an input file, all of which start with
the same 14 base pair fragment, write a program that will:
(a) Trim the sequence and and write the cleaned sequences to a new file
(b) Print the length of each sequence to the screen
"""

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for seq in infile:
        trimmed_seq = seq[14:].strip()
        seq_length = len(trimmed_seq)
        print(seq_length)
        outfile.write(trimmed_seq + "\n")
