"""
Write a program that will create a FASTA file for the three sequences given in the book
Make sure that all sequences are in upper case and only contain A, T, G and C
"""

# Dictionary to store the sequences given in the book
seqs = {
    "ABC123": "ATCGTACGATCGATCGATCGCTAGACGTATCG",
    "DEF456": "actgatcgacgatcgatcgatcacgact",
    "HIJ789": "ACTGAC-ACTGT--ACTGTA----CATGTG",
}

# I/O
with open("seqs.fasta", "w") as outfile:
    for header, seq in seqs.items():
        # Ensure that all sequences are in uppercase
        uppercase_seq = seq.upper()
        # Ensure that they only contain A, T, G and C
        removed_dashes_seq = uppercase_seq.replace("-", "")
        outfile.write(f">{header}\n{removed_dashes_seq}\n")
