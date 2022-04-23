""" 
See more (including information on k-mers and a sample dataset) at https://rosalind.info/problems/kmer/
PROBLEM
For a fixed positive integer k, order all possible k-mers taken from an underlying alphabet lexicographically. Then the k-mer composition of a string s can be represented by an array A for which A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic order) appears in s.
Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.

-------------------------------- MY SOLUTION ------------------------------

"""

import regex as re
from itertools import product as prod

with open('rosalind_kmer.txt') as file:  # read fasta file, ouput: DNA as a string
    string = ''
    for line in file:
        if not line[0] == '>':
            string += line.rstrip()

alphabet = ['A', 'C', 'G', 'T']        # find all 4-mers that exist
kmers = []
for i in prod(alphabet, repeat=4):
    kmers.append(''.join(i))

composition = []         # count the number of times that each kmer appear in the string, overlapping included
for kmer in kmers:
    count_matches = len(re.findall(kmer, string, overlapped = True))
    composition.append(str(count_matches))

' '.join(composition)