# Define a function called find_cut_sites that takes:
#   A DNA sequence string
#   A recognition sequence string (the enzyme target)
# Check that both strings contain only A, C, G, or T (uppercase or lowercase allowed)
# Scan the DNA sequence and find all start positions where the recognition sequence matches
# Return a list of integer positions (0-based indexing)
# Demonstrate usage with a sample input and print the result

def find_cut_sites(dna, recognition):
    # Standardize to uppercase
    dna = dna.upper()
    recognition = recognition.upper()

    # Validate characters
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    if not set(dna).issubset(valid_nucleotides):
        raise ValueError("DNA sequence contains invalid characters.")
    if not set(recognition).issubset(valid_nucleotides):
        raise ValueError("Recognition sequence contains invalid characters.")

    # Search for match positions
    cut_sites = []
    for i in range(len(dna) - len(recognition) + 1):
        if dna[i:i + len(recognition)] == recognition:
            cut_sites.append(i)
    return cut_sites


# Example usage
try:
    result = find_cut_sites("ATCCGGTACGTAGGTCAGCCGGTTCCGG", "CCGG")
    print("Cut sites found at positions:", result)
except ValueError as e:
    print("Error:", e)
