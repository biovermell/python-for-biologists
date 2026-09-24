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
### Exercise 02: Multiple exons from genomic DNA (`ex02_multiple_exon_extraction.py`)
- [ ] Turn nested code into functions
- [ ] Resolve discrepancy between 0-based and 1-based indexing
- [ ] Put file writing outside of loop (for better performance?)

## Chapter 05: Functions
### Exercise 01: percentage of aminoacid residues (`ex01_aminoacid_percentage.py`)
- [X] Fix typo in name of file (aminoacid -> amino acid)
- [X] Harmonize structure of multi-part exercise docstrings
- [X] Verify that helper function works as intended
- [X] Write a working main function
- [ ] Apply proper function annotation and type hinting, if deemed necessary
- [ ] Improve variable names to make them coherent with biological terms (e.g. residue vs. aa) and within the code (e.g. uppercase_aa vs. upper_aa)
- [ ] Reduce big block of assertions - use pytest?

## Chapter 06: Conditionals
### Exercise 01: Several species (`ex01_several_species.py`)
- [ ] Compare against textbook approach (give a name to each column, such as `species = columns[0]`) and decide which one is more efficient and readable
- [ ] Look into csv module
### Exercise 02: Length range (`ex02_length_range.py`)
- [ ] Compare against textbook approach (give a name to each column, such as `species = columns[0]`) and decide which one is more efficient and readable
- [ ] Ensure inequality covers correct range, without desired bases being excluded or undesired being included
- [ ] Make inequality syntax cleaner
- [X] Check that script complies with PEP8
### Exercise 03: AT content (`ex03_at_content.py`)
- [ ] Make variable names self-explanatory
- [X] Check that script complies with PEP8

## Chapter 07: Regular expressions
### Exercise 01: Accession names (`ex01_accession_names.py`)
- [ ] Solve exercise
- [ ] Improve output format - either store hits in a list for every condition (e. g. "Contain the number 5: xkn59438, hedle3455, xjhd53e, 45da") or make scrip interactive (e. g. "Select condition" -> "The names that fulfill the condition {contain the number 5} are xkn59438, hedle3455, xjhd53e, 45da") and so on
- [ ] Refactor so there aren't multiple loops in the code

# Repository-wide
- [ ] Add unit testing?
- [ ] Format all/most outputs as f-strings?
- [ ] Annotate all functions?
- [ ] Improve readability in all scripts by adding spaces and comments

# Docs
- [ ] Link to corresponding exercises in TODO