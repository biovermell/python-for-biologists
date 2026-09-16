"""
Chapter 06, exercise 02: Length range
Given a .csv file containing made-up data for a number of genes,
print out the gene names for all genes between 90 and 110 bases long
"""

with open("data.csv", "r") as infile:
    for line in infile:
        data = line.strip().split(",")
        if len(data[1]) > 90 and len(data[1]) < 110:
            gene_names = data[2]
            print(gene_names)