"""
Given DNA sequences from an input file, all of which start with the same 14 base pair fragment, write a program that will:
(a) Trim the sequence and and write the cleaned sequences to a new file
(b) Print the length of each sequence to the screen
"""

with open("input.txt", "r") as infile:
    for seq in infile:
        trimmed_seq = seq[14:]
    with open("output.txt", "w") as outfile:
        outfile.write(trimmed_seq)

with open("output.txt", "r") as infile:
    for seq in infile:
        seq_length = len(seq)
        print(seq_length)
