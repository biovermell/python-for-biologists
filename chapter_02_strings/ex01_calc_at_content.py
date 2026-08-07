"""
Chapter 02, exercise 01: Calculating AT content
Given a short DNA sequence, write a program that will
print out its AT content
"""

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

at_content = ((seq.count("A") + seq.count("T")) * 100) / len(seq)

# Formated so only two decimal places are shown
print(f"{at_content:.2f}%")
