"""
Write a program that will create a FASTA file for each of the three sequences given in the book.
The names of the files should be the same as the sequence header names, with the extension .fasta
Make sure that all sequences are in upper case and only contain A, T, G and C
"""

# Dictionary to store the sequences given in the book
seqs = {
    "ABC123": "ATCGTACGATCGATCGATCGCTAGACGTATCG",
    "DEF456": "actgatcgacgatcgatcgatcacgact",
    "HIJ789": "ACTGAC-ACTGT--ACTGTA----CATGTG",
}

# I/O
for header, seq in seqs.items():
    # Ensure that all sequences are in uppercase
    uppercase_seq = seq.upper()
    # Ensure that they only contain A, T, G and C
    removed_dashes_seq = uppercase_seq.replace("-", "")
    with open(header + ".fasta", "w") as outfile:
        outfile.write(f">{header}\n{removed_dashes_seq}\n")
