#import necessary libraries
import re

# Compile a regex to find a TATA box in the sequence (example pattern)
tata_box_regex = re.compile(r'TATA[AT]A[AT]')
# Compile a regex to extract the ID after 'gene:' in the header
gene_id_regex = re.compile(r'gene:([^ \t]+)')

# Initialize storage for gene IDs that contain a TATA box
genes = []
# Track the current gene’s ID and its sequence
current_gene_name = ""
current_sequence = ""

# Open the input FASTA file
with open('sequence.fa', 'r') as infile:
    for line in infile:
        line = line.rstrip('\n')
        if line.startswith('>'):
            # If we’ve read a gene and its sequence contains a TATA box,
            # save that gene’s ID before moving on
            if current_gene_name and tata_box_regex.search(current_sequence):
                genes.append(current_gene_name)

            # Extract the gene ID from the header line (after 'gene:')
            match = gene_id_regex.search(line)
            if match:
                current_gene_name = match.group(1)
            else:
                # Fallback: take the first whitespace-delimited token (minus the '>')
                current_gene_name = line[1:].split()[0]

            # Reset the sequence accumulator for the next gene
            current_sequence = ""
        else:
            # Append sequence lines (stripping out any whitespace/newlines)
            current_sequence += line.strip()

# After the loop, check the very last gene the same way
if current_gene_name and tata_box_regex.search(current_sequence):
    genes.append(current_gene_name)

# Write each matching gene ID to the output file, one per line
with open('tata_genes.fa', 'w') as outfile:
    for gene in genes:
        outfile.write(f">{gene}\n")