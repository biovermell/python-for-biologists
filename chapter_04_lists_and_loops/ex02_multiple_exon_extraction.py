"""
Given a file with a section of genomic DNA and a file with a list
of start/stop positions of exons, write a program that will extract
the exon segments, concatenate them, and write them to a new file.

Each exon is on a separate line and the start and stop
positions are separated by a comma.
"""

with (
    open("genomic_dna.txt", "r") as dnainfile,
    open("exons.txt", "r") as exoninfile,
    open("extracted_dna.txt", "w") as outfile,
):
    seq = dnainfile.read().strip()
    for line in exoninfile:
        exon_coordinates = line.split(",")
        start = int(exon_coordinates[0])
        stop = int(exon_coordinates[1])
        exon = seq[start:stop]
        outfile.write(exon)
