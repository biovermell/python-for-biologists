"""
Chapter 02, exercise 04: Splicing out introns
Given a DNA sequence that comprises two exons and an intron, write a program that will:
- Part one: Print just the  coding regions of the DNA sequence
- Part two: Calculate what percentage of the sequence is coding
- Part three: Print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase

The first exon runs from the start of the sequence to the 63rd character, and the second runs from the 91st character to
the end of the sequence
"""

# PART ONE

seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = seq[0:63]
exon2 = seq[90:]

coding_region = exon1 + exon2

print(coding_region)

# PART TWO

coding_percentage = (len(coding_region) * 100) / len(seq)

print(coding_percentage)
