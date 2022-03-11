

codon = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
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

import re
fas = open("rosalind_splc.txt", 'r').read()
trim= fas.replace('\n','')
split = re.split('>',trim)[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)
dna = file[0]
intron = file[1:]

for i in intron:
    dna = dna.replace(i, '')

rna = dna.replace("T", "U")

protein = []
for i in range(0,len(rna),3):
    if trans[rna[i:i+3]] != 'Stop':
        protein.append(trans[rna[i:i+3]])
    else:
        break
print(''.join(protein))

