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

hydrophobic_aa = ["A", "I", "L", "M", "F", "W", "Y", "V"]


# HELPER FUNCTION
# Iterates through the list of aa and turns them to uppercase
def uppercase_aa(aa):
    upper_aa = []
    for residue in aa:
        upper_residue = residue.upper()
        upper_aa.append(upper_residue)
    return upper_aa


# MAIN FUNCTION
def amino_acid_percentage(prot_seq, aa=hydrophobic_aa):
    upper_prot_seq = prot_seq.upper()
    uppercase_aa(aa)
    residue_count = upper_prot_seq.count(residue)
    aa_percentage = (residue_count * 100) / len(upper_prot_seq)
    return aa_percentage


# GIVEN ASSERTIONS
# PART ONE
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

# PART TWO
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]) == 55
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]) == 70
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP") == 65
