"""
Chapter 06, exercise 05: High low medium
Given a .csv file containing made-up data for a number of genes,
print out a message giving the gene name and saying whether its
AT content is high (greater than 0.65), low (less than 0.45) or
medium (between 0.45 and 0.65).
"""


# AT calculation function
def at_content(seq):
    seq = seq.upper()
    return (seq.count("A") + seq.count("T")) / len(seq)


with open("data.csv", "r") as infile:
    for line in infile:
        data = line.strip().split(",")
        seq = data[1]
        name = data[2]
        seq_at_content = at_content(seq)
        if seq_at_content > 0.65:
            print(f"{name}: high AT content ({seq_at_content:.2f})")
        elif 0.45 < seq_at_content < 0.65:
            print(f"{name}: medium AT content ({seq_at_content:.2f})")
        elif seq_at_content < 0.45:
            print(f"{name}: low AT content ({seq_at_content:.2f})")
