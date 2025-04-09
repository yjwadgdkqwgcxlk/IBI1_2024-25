# define the function with its two parameters
def finding_cut_sites(dna,recognition):
    #creat the array for cut sequence
    cut_sites = []
    #creat for range to check the whole dna sequence for the enzyme recognition sequence
    for i in range(len(dna)-len(recognition)+1):
        if dna[i: i + len(recognition)] == recognition:
            cut_sites.append(i)
    return cut_sites

#an application sample
p = finding_cut_sites( "ATCCGGTACGTAGGTCAG", "CCGG")
print (p)

