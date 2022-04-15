# See more (including information on open reading frames and a sample dataset) 
# at https://rosalind.info/problems/orf/

# PROBLEM
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. 
# Strings can be returned in any order.

# --------------------- MY SOLUTION ----------------------


rna_table = """                                # process rna codon table provided by Rosalind as a string
UUU F      CUU L      AUU I      GUU V         # convert it to a dictionary
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
UGG W      CGG R      AGG R      GGG G"""
d1 = rna_table.split()
rna_table = dict(zip(d1[0::2], d1[1::2]))


fas = open("rosalind_orf.txt", 'r').read()         # process fasta file and convert it to a string
trim= fas.replace('\n','')
dna = trim[14:]               # remove the name of DNA string e.g Rosalind_1234


def reverse(dna):
    """ Find the reverse complement of a dna string """
    trans = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    reverse_dna = ''
    for base in dna:
        reverse_dna += trans[base]
    return reverse_dna


def proteins(t):
    t = t.replace('T', 'U')      # dna to rna
    start_positions = []
    for i in range(len(t)):
        if t[i: i+3] == 'AUG':
            start_positions.append(i)
  
    reads = []
    for start in start_positions:
        readingframe = t[start:]
        stop = 0
        for i in range(0, len(readingframe), 3):
            if readingframe[i: i+3] in ['UAA', 'UGA', 'UAG']:
                stop += i
                break
        read = readingframe[:stop]    
        reads.append(read)    
     
    proteins = []
    for read in reads:
        aachain = ''
        for i in range(0, len(read), 3):
            if len(read[i: i+3]) == 3:
                aachain += rna_table[read[i: i+3]]
        proteins.append(aachain)
    return proteins 


prs1 = proteins(dna)
prs2 = proteins(reverse(dna))
prs = list(filter(None, set(prs1 + prs2)))      # prs1 and prs2 may share some proteins (or empty strings) 
for pr in prs:                                  # => convert the output list to a set object and filter out empty strings
    print(pr)     # this makes the output match the format required by Rosalind
