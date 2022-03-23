#     See more (including related information and sample datasets) at https://rosalind.info/problems/tran/

#     PROBLEM:
#     For DNA strings s1 and s2 having the same length, 
#     their transition/transversion ratio R(s1,s2) is the ratio of 
#     the total number of transitions to the total number of transversions 
#     Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp) (fasta format)
#     Return: The transition/transversion ratio R(s1,s2).

#_____________________________________ MY SOLUTION ________________________________________


import re                                                  # dealing with fasta format
fas = open("rosalind_tran.txt", 'r').read()
trim= fas.replace('\n','')
split = re.split('>',trim)[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)

a, b = file[0], file[1]                                     # the two DNA strings are put in a list
transi = {"A": "G", "G": "A", "C": "T", "T": "C"}

count_transver = 0
count_transi = 0

for i in range(len(a)):
    if transi[a[i]] == b[i]:
        count_transi += 1
    elif a[i] != b[i]:                  # take a look at the transition/transversion chart of Rosalind: A <-> G and C <-> T are transitions, the rest are transversions
        count_transver += 1                
    
print(count_transi/count_transver)
