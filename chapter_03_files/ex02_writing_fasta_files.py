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

for header, seq in seqs.items():
    # Ensure that all sequences are in uppercase
    uppercase_seq = seq.upper()
    # Ensure that they only contain A, T, G and C
