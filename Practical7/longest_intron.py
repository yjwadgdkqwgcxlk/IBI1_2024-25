#set the sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

#set the initial values for the variables
max_length = 0 #the maximum length of the intron
start_index = 0 #the starting index of the intron

#look for "GT" and "AG"
while True:
    gt_index = seq.find('GT', start_index)  # localise GT
    if gt_index == -1:  # if GT not found, exit loop
        break
    else:  # if GT found, look for AG
        ag_index = seq.find('AG', gt_index + 2)  # find AG after GT
        if ag_index == -1:  # if AG not found, exit loop
            break
        else: 
            intron_length = ag_index - gt_index + 2  # calculate intron length
            if intron_length > max_length:  # update max_length if longer intron found
                max_length = intron_length
            start_index = ag_index + 2  # update start_index for next iteration

#print the result
print ('The longest intron has length', max_length)
    
