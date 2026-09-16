"""
Chapter 06, exercise 03: AT content
Given a .csv file containing made-up data for a number of genes,
print out the gene names for all genes whose AT content is less 
than 0.5 and whose expression level is greater than 200
"""

# AT calculation function
def at_content(seq):
    seq = seq.upper()
    return (seq.count("A") + seq.count("T")) / len(seq)

with open("data.csv", "r") as infile:
    for line in infile:
        data = line.strip().split(",")
        seq = data[1]
        if int(data[3]) > 200 and at_content(seq) < 0.5:
            gene_names = data[2]
            print(gene_names)