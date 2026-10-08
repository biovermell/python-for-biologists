"""
Chapter 08, exercise 01: DNA translation
Write a program that will translate a DNA sequence into protein.
Your program should use the standard genetic code which can be found at:
http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1

Note: To solve this exercise, I have used the same dna.txt file from ch07 ex02
"""

# DICTIONARY
standard_code = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


# HELPER FUNCTION
def codon_checker(seq):
    if len(seq) % 3 == 0:
        return seq
    else:
        print(
            "Warning: Incomplete codons at the end of the sequence have been ommitted"
        )
        return seq[: len(seq) - (len(seq) % 3)]


# CORE LOGIC
def dna_translation(seq):
    seq = codon_checker(seq)
    protein = ""
    for number in range(0, len(seq), 3):
        codon = seq[number : number + 3]
        aa = standard_code.get(codon, "X")
        protein += aa
    print(f"The amino acid sequence is {protein}")


# EXECUTION
with open("dna.txt", "r") as infile:
    seq = infile.readline().strip().upper()
    dna_translation(seq)
