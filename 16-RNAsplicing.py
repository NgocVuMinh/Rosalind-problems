#     See more (including information on discontiguous genes and sample datasets) at https://rosalind.info/problems/splc/

#     PROBLEM:
#     After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
#     Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#     Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

#     !!! NOTICE that the actual dataset that Rosalind gives you is in FASTA format so it looks something more like this (need to take into account the seperated lines):
#     >Rosalind_1
#     ATCCAGCT
#     GGGCAACT
#______________________________ MY SOLUTION _________________________________


codon = """
UUU F      CUU L      AUU I      GUU V                          # Rosalind provides the (RNA-to-protein) codon table as a string.
UUC F      CUC L      AUC I      GUC V                          # converting this string into a dictionary
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
""".split()
trans = dict(zip(codon[0::2], codon[1::2]))

import re                                                       # dealing with the fasta format
fas = open("rosalind_splc.txt", 'r').read()
trim= fas.replace('\n','')
split = re.split('>',trim)[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)
dna = file[0]                                                   # the final list has the dna at index=0, and the rest are introns
intron = file[1:]

for i in intron:                                                # remove introns in dna by replace them with '' (blank)
    dna = dna.replace(i, '')

rna = dna.replace("T", "U")                                     # translate dna to rna

protein = []                                                    # translate rna to protein
for i in range(0,len(rna),3):
    if trans[rna[i:i+3]] != 'Stop':
        protein.append(trans[rna[i:i+3]])
    else:
        break
print(''.join(protein))

