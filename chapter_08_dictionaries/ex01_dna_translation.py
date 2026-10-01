"""
Chapter 08, exercise 01: DNA translation
Write a program that will translate a DNA sequence into protein.
Your program should use the standard genetic code which can be found at:
http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1

Note: To solve this exercise, I have used the same dna.txt file from ch07 ex02
"""

# DICTIONARY
standard_code = {
    "TTT": "F",
    "TCT": "S",
    "TAT": "Y",
    "TGT": "C",
    "TTA": "L",
    "TCA": "S",
    "TAA": "STOP",
    "TGA": "STOP",
    "TTG": "L",
    "TCG": "S",
    "TAG": "STOP",
    "TGG": "W",
    "CTT": "L",
    "CCT": "P",
    "CAT": "H",
    "CGT": "R",
    "CTC": "L",
    "CCC": "P",
    "CAC": "H",
    "CGC": "R",
    "CTA": "L",
    "CCA": "P",
    "CAA": "Q",
    "CGA": "R",
    "CTG": "L",
    "CCG": "P",
    "CAG": "Q",
    "CGG": "R",
    "ATT": "I",
    "ACT": "T",
    "AAT": "N",
    "AGT": "S",
    "ATC": "I",
    "ACC": "T",
    "AAC": "N",
    "AGC": "S",
    "ATA": "I",
    "ACA": "T",
    "AAA": "K",
    "AGA": "R",
    "ATG": "M",
    "ACG": "T",
    "AAG": "K",
    "AGG": "R",
    "GTT": "V",
    "GCT": "A",
    "GAT": "D",
    "GGT": "G",
    "GTC": "V",
    "GCC": "A",
    "GAC": "D",
    "GGC": "G",
    "GTA": "V",
    "GCA": "A",
    "GAA": "E",
    "GGA": "G",
    "GTG": "V",
    "GCG": "A",
    "GAG": "E",
    "GGG": "G",
}


# HELPER FUNCTIONS
def codon_checker(seq):
    if len(seq) / 3 == 0:
        pass
    else:
        print(
            "Warning: Incomplete codons at the end of the sequence have been ommitted"
        )


# CORE LOGIC
def dna_translation(seq):
    pass


# EXECUTION
with open("dna.txt", "r") as infile:
    seq = infile.readline().strip()
