This document tracks necessary improvements that fall within the scope of the exercise. For plans and improvements that go beyond what is asked in the exercise, see [ROADMAP.md](./ROADMAP.md)

# Exercise-specific
## Chapter 02: Printing and manipulating text
### Exercise 03: Restriction fragment lengths (`ex03_restriction_fragments.py`)
- [X] Improve core logic so restriction site isn't removed from sequence
- [X] Make code more readable by improving variable names 
### Exercise 04: Splicing out introns (`ex04_splicing_out_introns.py`)
- [ ] Improve output format
- [ ] Resolve discrepancy between results from my solution and the textbook's solution

## Chapter 03: Reading and writing files
### Exercise 01: Splitting genomic DNA (`ex01_splitting_genomic_dna.py`)
- [ ] Turn top-down script into functions?
### Exercise 02: Writing FASTA files (`ex02_writing_fasta_files.py`)
- [ ] Turn top-down script into functions
- [ ] Improve sequence cleaning logic to truly ensure that only valid bases are present in the sequence instead of just removing the dashes
- [ ] Fix script so sequences aren't hardcoded?
### Exercise 03: Writing multiple FASTA files (`ex03_writing_multiple_fasta_files.py`)
- [ ] Turn top-down script into functions
- [ ] Improve sequence cleaning logic to truly ensure that only valid bases are present in the sequence instead of just removing the dashes
- [ ] Fix script so sequences aren't hardcoded?

## Chapter 04: Lists and loops
### Exercise 01: Processing DNA in a file (`ex01_processing_dna_in_a_file.py`)
- [X] Fix core logic so output file isn't overwritten in each iteration of the loop
- [ ] Turn nested code into functions
- [ ] Improve variable names to make code more readable
### Exercise 02: Multiple exons from genomic DN (`ex02_multiple_exon_extraction.py`)
- [ ] Turn nested code into functions
- [ ] Resolve discrepancy between 0-based and 1-based indexing
- [ ] Put file writing outside of loop (for better performance?)

## Chapter 05: Functions
### Exercise 01: percentage of aminoacid residues (`ex01_aminoacid_percentage.py`)
- [X] Fix typo in name of file (aminoacid -> amino acid)
- [X] Harmonize structure of multi-part exercise docstrings
- [ ] Solve exercise

# Repository-wide
- [ ] Add unit testing?
- [ ] Format all/most outputs as f-strings?
