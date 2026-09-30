"""
Chapter 07, exercise 02: Double digest
Given a file with a DNA sequence, predict the
fragment lengths that we will get if we digest the
sequence with two made-up restriction enzymes – AbcI,
whose recognition site is ANT*AAT, and AbcII, whose
recognition site is GCRW*TG
Asterisks indicate the position of the cut site
"""

import re


# CORE LOGIC
def restriction_enzymes(seq):
    abci = re.split(r"(?<=A[ATGC]T)(?=AAT)", seq)
    abcii = re.split(r"(?<=GC[AG][AT])(?=TG)", seq)
    frags = [abci, abcii]
    return frags


# I/0
with open("dna.txt", "r") as infile:
    seq = infile.readline().strip()
    # "Digest" the seq by calling restriction_enzymes
    # Ideally, would give a list with the frags as output
    restriction_enzymes(seq)
    # Gives number of frags
    number_of_frags = len(frags)
    # Gives length of each frag
    frag_lenghts = []
    for frag in frags:
        frag_lenghts.append(len(frag))
    print(f"The sequence has {number_of_frags} fragments of lengths {frag_lenghts}")
