# Ask user to input one of the three splice site combinations (GTAG, GCAG, ATAC)
# Read in FASTA file 'sequence.fa', extract gene names and sequences
# For each gene:
#   Check if sequence contains the chosen splice combination
#   If yes, check for TATA box matches using regex TATA[AT]A[AT]
#   If TATA matches found, write to output FASTA file:
#   >GENE_NAME|TATA_count
#   FULL_SEQUENCE (no line breaks)

import re

# Step 1: Get valid splice site input from user
valid_combinations = ['GTAG', 'GCAG', 'ATAC']
splice_combination = input("Enter splice combination (GTAG, GCAG, ATAC): ").upper()

while splice_combination not in valid_combinations:
    splice_combination = input("Invalid input. Please enter GTAG, GCAG, or ATAC: ").upper()

output_filename = f"{splice_combination}_spliced_genes.fa"

# Step 2: Prepare to store matching gene info
gene_data = []

try:
    with open('sequence.fa', 'r') as file:
        current_name = ""
        current_seq = ""

        for line in file:
            if line.startswith('>'):
                # Store previous gene if it matches
                if current_name and splice_combination in current_seq:
                    tata_matches = re.findall(r'TATA[AT]A[AT]', current_seq)
                    if tata_matches:
                        tata_count = len(tata_matches)
                        gene_data.append((current_name, tata_count, current_seq))

                # Extract gene name
                match = re.search(r'gene:(\S+)', line)
                current_name = match.group(1) if match else "Unknown"
                current_seq = ""
            else:
                current_seq += line.strip().upper()

        # Final gene
        if current_name and splice_combination in current_seq:
            tata_matches = re.findall(r'TATA[AT]A[AT]', current_seq)
            if tata_matches:
                tata_count = len(tata_matches)
                gene_data.append((current_name, tata_count, current_seq))

except FileNotFoundError:
    print("The file 'sequence.fa' is not found!")
    exit()

# Step 3: Write to output FASTA file
with open(output_filename, 'w') as output_file:
    for name, tata_count, seq in gene_data:
        output_file.write(f">{name}|{tata_count}\n{seq}\n")
