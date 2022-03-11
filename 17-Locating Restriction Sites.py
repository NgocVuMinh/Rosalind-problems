#     See more (including related information and sample datasets) at https://rosalind.info/problems/revp/

#     PROBLEM:
#     A DNA string is a reverse palindrome if it is equal to its reverse complement. 
#     For instance, GCATGC is a reverse palindrome because its reverse complement is also GCATGC. 
#     Given: A DNA string of length at most 1 kbp in FASTA format.
#     Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

#     !!! NOTICE that the actual dataset that Rosalind gives you is in FASTA format, so it looks something more like this (need to take into account the seperated lines):
#     >Rosalind_24
#     TCAATGCATGCGGGTCTATATGCAT
#     GCGGGTCTATATGCATTCAATGCAT
#     TAGCTGATCGATCGTGCGATC
#_____________________________________ MY SOLUTION ________________________________________


fas = open('rosalind_revp.txt').read()                      #dealing with fasta format
dna = fas.replace('\n', '')[14:]

def complement(dna):                                        #find the complementary strand
    trans = {'A': 'T', 'T': 'A', 'G': 'C', 'C':'G'}
    DNAcom = []
    for base in dna:
        DNAcom.append(trans[base])
    return ''.join(DNAcom)
    
def palindrome(dna):                                        #finding the reverse palindrome
    for i in range(len(dna)):
        for j in range(i,len(dna)+1):
            a = dna[i:j]
            b = complement(a)[::-1]
            if (a == b) and (len(a) > 3) and (len(a) < 13):
                print(i+1, len(a))

print(palindrome(dna))
