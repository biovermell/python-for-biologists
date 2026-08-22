"""
Write a program that will split the DNA from genomic_dna.txt into coding and non-coding parts, and write these sequences
to two separate files.

The first exon runs from the start of the sequence to the 63rd character, and the second runs from the 91st character to
the end of the sequence
"""

with open("genomic_dna.txt", "r") as infile:
    seq = infile.read().strip()

exon1 = seq[0:63]
exon2 = seq[90:]
intron = seq[63:90]

coding_region = exon1 + exon2

with open("coding_region.txt", "w") as outfile:
    outfile.write(coding_region)

with open("non_coding_region.txt", "w") as outfile:
    outfile.write(intron)
