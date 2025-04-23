#import necessay libraries
import re

# valid splice sites
valid_combinations = ['GTAG', 'GCAG', 'ATAC']

# user input
splice_combination = input("Enter splice combination (GTAG, GCAG, ATAC): ").upper()
while splice_combination not in valid_combinations:
    splice_combination = input("Invalid input. Please enter GTAG, GCAG, or ATAC: ").upper()

# output filename
output_filename = f"{splice_combination}_spliced_genes.fa"

gene_data = []

try:
    with open('sequence.fa', 'r') as file:
        current_name = ""
        current_seq = ""

        for line in file:
            if line.startswith('>'):
                if current_name and splice_combination in current_seq:
                    gene_data.append((current_name, current_seq))

                # extract gene name after 'gene:'
                match = re.search(r'gene:(\S+)', line)
                current_name = match.group(1) if match else "Unknown"
                current_seq = ""
            else:
                current_seq += line.strip().upper()

        # append the last gene
        if current_name and splice_combination in current_seq:
            gene_data.append((current_name, current_seq))

except FileNotFoundError:
    print("The file is not found!")
    exit()

# write output in format: gene_name, sequence, TATA count
with open(output_filename, 'w') as output_file:
    for name, seq in gene_data:
        tata_count = len(re.findall(r'(?i)TATA', seq))
        if tata_count > 0:
            output_file.write(f">{name} | TATA count: {tata_count}\n{seq}\n")