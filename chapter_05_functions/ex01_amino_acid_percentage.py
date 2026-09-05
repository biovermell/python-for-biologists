"""
Chapter 05, exercise 01: Percentage of amino acid residues
Write a function that:
- Part one: Takes a protein sequence and an amino acid residue code
as arguments and returns the percentage of the protein that the
amino acid makes up
- Part two: Modify the function from part one so that
it accepts a list of amino acid residues rather than a single one.
If no list is given, the function should return the
percentage of hydrophobic amino acid residues (A, I, L, M, F, W,
Y and V)

Use the given assertions to test the function
"""


# aa stands for amino acid
def amino_acid_percentage(prot_seq, aa):
    aa_count = prot_seq.count(aa.upper())
    aa_percentage = (aa_count * 100) / len(prot_seq)
    return aa_percentage


# GIVEN ASSERTIONS
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
