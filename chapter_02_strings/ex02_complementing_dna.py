"""
Chapter 02, exercise 02: Complementing DNA
Given a short DNA sequence, write a program that will
print the complement of this sequence
"""

# Requires Python 3 to run

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


def seq_complement(seq):
    complement_table = str.maketrans("ACGT", "TGCA")
    return seq.translate(complement_table)


print(seq_complement(seq))
