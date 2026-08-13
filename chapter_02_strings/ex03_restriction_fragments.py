"""
Chapter 02, exercise 03: Restriction fragment lengths
Given a short DNA sequence with a recognition site for EcoRI,
write a program that will calculate the size of the fragments
that will be produced when the sequence is digested with EcoRI
"""

seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"


# Addition of 1 corrects for Python's 0-based counting
frag1 = seq.find("GAATTC") + 1

frag2 = len(seq) - frag1

# This line can handle cases where there is more than one restriction site
number_of_fragments = len(seq.split("GAATTC"))

# Prints number of fragments along with the length of each one
print(
    f"The sequence has {number_of_fragments} fragments of length {frag1} and {frag2} respectively"
)
