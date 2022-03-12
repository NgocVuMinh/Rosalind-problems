# See more (including information on modular arithmetic and sample datasets) at https://rosalind.info/problems/mrna/

# PROBLEM:
# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
#         (Don't neglect the importance of the stop codon in protein translation.)

# NOTICE: 1. the codon table is provided my Rosalind as a string.
#         2. the dataset provided my Rosalind has an empty line at the bottom ('\n'), this needs removing.

#________________________________________ MY SOLUTION __________________________________________


codons = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
CAA Q      AAA K      GAA E      CAG Q      
AAG K      GAG E      UGU C      CGU R      
AGU S      GGU G      UGC C      CGC R      
AGC S      GGC G      CGA R      AGA R      
GGA G      UGG W      CGG R      AGG R      
GGG G"""

trans = codons.split()
table = dict(zip(trans[0::2], trans[1::2]))

def getRNA(x):                                                              # return all possible RNA of each protein
    return len([key for key, value in table.items() if x in value])

protein = (open('rosalind_mrna.txt', 'r')).read().strip()                   # strip() removes the extra '\n'
count = []
for aa in protein:
    count.append(getRNA(aa))

import math                                                 # math.prod() multiplies all numbers in the list, there are 3 possible stop codons so *3
print((3*math.prod(count))%1000000)
