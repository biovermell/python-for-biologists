"""
Chapter 02, exercise 03: Restriction fragment lengths
Given a short DNA sequence with a recognition site for EcoRI,
write a program that will calculate the size of the fragments
that will be produced when the sequence is digested with EcoRI
"""

seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut = seq.split("GAATTC")
# The .split method removes "GAATTC" from the sequence

# Add 1 and 5 to correct removed bases
number_of_fragments = len(cut)
length_frag1 = len(cut[0]) + 1
length_frag2 = len(cut[1]) + 5

# Prints number of fragments along with the length of each
print(
    f"The sequence has {number_of_fragments} fragments of length {length_frag1} and {length_frag2} respectively"
)
