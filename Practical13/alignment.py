# Comparing three sequences: human SOD2 (P04179), mouse SOD2 (P09671), and a random protein.
# Sequences are in FASTA format and of the same length.
# Also using a BLOSUM62 substitution matrix from a text file.
# For each pair, I’ll calculate alignment score and % identity using a non-gapped global alignment.

# Read three protein sequences from FASTA files: human, mouse, random
# Read BLOSUM62 substitution matrix from text file
# For each pairwise comparison:
#     Compare aligned amino acids one by one
#     Add BLOSUM score and count identical matches
#     Calculate total score and percentage identity
# Print the comparison name, score, and identity

def read_fasta(file):
    with open(file) as f:
        lines = f.readlines()
    name = lines[0].strip().replace(">", "")
    seq = "".join([line.strip() for line in lines[1:]])
    return name, seq

def load_blosum62(file):
    matrix = {}
    with open(file) as f:
        lines = f.readlines()
    header = lines[0].split()
    for line in lines[1:]:
        parts = line.split()
        row_aa = parts[0]
        scores = parts[1:]
        for i in range(len(scores)):
            col_aa = header[i]
            val = int(scores[i])
            matrix[(row_aa, col_aa)] = val
            matrix[(col_aa, row_aa)] = val
    return matrix

def align(seq1, seq2, blosum):
    score = 0
    identical = 0
    for a1, a2 in zip(seq1, seq2):
        score += blosum.get((a1, a2), -4)
        if a1 == a2:
            identical += 1
    identity = identical / len(seq1) * 100
    return score, identity

# Load sequences from your actual filenames
name1, seq1 = read_fasta("P04179.fasta")           # human
name2, seq2 = read_fasta("P09671.fasta")           # mouse
name3, seq3 = read_fasta("random_protein.fasta")   # random

# Load BLOSUM62 matrix
blosum = load_blosum62("BLOSUM62.txt")

# Compare and print results
pairs = [
    (name1, seq1, name2, seq2),
    (name1, seq1, name3, seq3),
    (name2, seq2, name3, seq3)
]

for n1, s1, n2, s2 in pairs:
    score, identity = align(s1, s2, blosum)
    print()
    print(f"{n1} vs {n2}")
    print("Score:", score)
    print(f"Identity: {identity:.2f}%")