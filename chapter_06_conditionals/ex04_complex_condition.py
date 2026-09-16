"""
Chapter 06, exercise 04: Complex condition
Given a .csv file containing made-up data for a number of genes,
print out the gene names for all genes whose name begins with 
"k" or "h" except those belonging to Drosophila melanogaster
"""

with open("data.csv", "r") as infile:
    for line in infile:
        if not line.startswith("Drosophila melanogaster"):
            data = line.strip().split(",")
            species = data[0]
            seq = data[1]
            name = str(data[2])
            expression = data[3]
            if name.startswith(("k", "h")):
                print(name)
