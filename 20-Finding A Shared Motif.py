""" 
See more (including information on motifs and a sample dataset) at https://rosalind.info/problems/lcsm/
PROBLEM
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s. 
Strings can be returned in any order.

-------------------------------- MY SOLUTION ------------------------------
I decided to adapt kmer-indexing, one of the methods that I learned in the course Algorithm for DNA sequencing
See more on this at: https://www.youtube.com/watch?v=2UsmUgJtwAI

"""

import re
fas = open('rosalind_lcsm.txt','r').read()               
trim = fas.replace('\n','')
split = re.split('>',trim)[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)

def all_kmers(read, k):
    """ Returns all k-mers of length k of a given read (string) """
    all_kmers = []
    for i in range(len(read) - k + 1):
        all_kmers.append(read[i: i+k])
    return all_kmers
    
def motif(a, b):
    """ Taking the first strand (a) , take all its kmers and see if each kmer is in 
    the remaining strands (list b) , if yes then append that kmer to a list of all motifs, 
    then return the longest kmer in that list """
    
    motifs = []
    for i in reversed(range(2, len(a))):
        kmers = all_kmers(a, i)
        for kmer in kmers:
            found = False
            for j in b:
                if kmer in j:
                    found = True
                    continue
                else:
                    found = False
                    break
            if found == True:
                motifs.append(kmer)
    motif = sorted(set(motifs), key = len)[-1]    # many kmers in the list are identical, 
    return motif                                  # so set() to only keep unique kmers, and sort them according to length 

motif(file[0], file[1:])