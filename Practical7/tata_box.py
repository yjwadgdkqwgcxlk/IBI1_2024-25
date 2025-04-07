import re

#define regular expression for TATA box
tata_box_regex = re.compile(r"TATA[AT]A[AT]")

genes = []

current_gene_name = ""
current_sequence = ""

# read the file and extract TATA box sequences
with open('sequence.fa', 'r') as file:     
    for line in file:
        if line.startswith('>'):  # start of a new gene
            # if current gene has TATA box, add it to the list
            if current_gene_name and tata_box_regex.search(current_sequence):
                genes.append((current_gene_name, current_sequence))

            # store the new gene name and reset sequence
            current_gene_name = line[1:].strip()  # remove the '>' and any surrounding whitespace
            current_sequence = ""  # reset the sequence
        else:
            current_sequence += line.strip()  # add sequence without newlines

# the last gene
if current_gene_name and tata_box_regex.search(current_sequence):
    genes.append((current_gene_name, current_sequence))

# put it to a file
with open('tata_genes.fa', 'w') as out_file:
    for gene_name in genes:
        out_file.write(f">{gene_name}\n")