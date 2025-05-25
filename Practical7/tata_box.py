# Read input FASTA file line by line
# For each gene:
#   Combine multiline sequences into a single string
#   Extract gene name using regex from the header
#   Check if sequence contains TATA box pattern TATA[AT]A[AT]
#   If match found, write gene name and full sequence to output file 'tata_genes.fa'

import re

# Compile TATA box pattern: TATA[AT]A[AT]
tata_box_regex = re.compile(r'TATA[AT]A[AT]')
# Compile pattern to extract gene name from header
gene_id_regex = re.compile(r'gene:([^ \t]+)')

# Initialize output storage
output = []

current_gene_name = ""
current_sequence = ""

# Read input FASTA file
with open('sequence.fa', 'r') as infile:
    for line in infile:
        line = line.rstrip('\n')
        if line.startswith('>'):
            # Process previous gene
            if current_gene_name and tata_box_regex.search(current_sequence):
                output.append((current_gene_name, current_sequence))

            # Extract gene name
            match = gene_id_regex.search(line)
            if match:
                current_gene_name = match.group(1)
            else:
                current_gene_name = line[1:].split()[0]

            # Reset sequence
            current_sequence = ""
        else:
            current_sequence += line.strip()

# Final gene check
if current_gene_name and tata_box_regex.search(current_sequence):
    output.append((current_gene_name, current_sequence))

# Write output FASTA file
with open('tata_genes.fa', 'w') as outfile:
    for name, seq in output:
        outfile.write(f">{name}\n{seq}\n")
