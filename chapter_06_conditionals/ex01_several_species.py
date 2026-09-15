"""
Chapter 06, exercise 01: Several species
Given a .csv file containing made-up data for a number of genes,
print out the gene names for all genes belonging to Drosophila
melanogaster or Drosophila simulans
"""

with open("data.csv", "r") as infile:
    for line in infile:
        if line.startswith(("Drosophila melanogaster", "Drosophila simulans")):
            data = line.strip().split(",")
            gene_names = data[2]
            print(gene_names)
