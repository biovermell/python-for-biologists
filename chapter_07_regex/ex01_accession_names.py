"""
Chapter 07, exercise 01: Accession names
Given a list of made-up gene accession names, write a
program that will print only the accession names that
satisfy the following criteria – treat each criterion separately:
a) contain the number 5
b) contain the letter d or e
c) contain the letters d and e in that order
d) contain the letters d and e in that order with a single letter between them
e) contain both the letters d and e in any order
f) start with x or y
g) start with x or y and end with e
h) contain three or more numbers in a row
i) end with d followed by either a, r or p
"""

import re

accession_names = [
    "xkn59438",
    "yhdck2",
    "eihd39d9",
    "chdsye847",
    "hedle3455",
    "xjhd53e",
    "45da",
    "de37dp",
]


def hardcoded_regex():
    # a) contain the number 5
    for name in accession_names:
        if re.search(r"5", name):
            print(f"{name} contains the number 5")

    # b) contain the letter d or e
    for name in accession_names:
        if re.search(r"[de]", name):
            print(f"{name} contains the letter d or e")

    # b) contain the letters d and e in that order
    for name in accession_names:
        if re.search(r"[d.*e]", name):
            print(f"{name} contains the letters d and e in that order")


hardcoded_regex()
