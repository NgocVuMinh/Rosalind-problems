# See more (including information on graph theory, overlap graphs and sample datasets) 
# at https://rosalind.info/problems/grph/

# PROBLEM
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

# --------------------- MY SOLUTION ----------------------

"""
Version 1: this version works well for small dataset (the one given by Rosalind is quite small ~100 reads)
For large dataset, the code will work but it will be very slow. For a better version for such situation, 
refer to version 2 below

"""

import re
from itertools import permutations as pmt

def readFasta(filename):
    """ Read file in FASTA format, return a list of all reads and a dictionary with keys as names of reads
    and items as reads"""
    readsDict = {}
    reads = []
    file = open(filename, 'r').read()
    reads_split = re.split('>', file)[1:]
    for i in range(len(reads_split)):
        reads_split[i] = reads_split[i].replace('\n', '')
    for read in reads_split:
        readsDict[read[:13]] = read[13:]      # read[:13] is the name of the read, eg Rosalind_1234
        reads.append(read[13:])
    return reads, readsDict

def readsName(myread, readsDict):
    """ Given a read and a dictionary (refer to the function above), return the name of that read """
    reads = readsDict.items()
    for read in reads:
        if read[1] == myread:
            name = read[0]
    return name

def overlap(a, b, k):
    """ Given two reads a and b and a length of k bases, return k if a suffix of a match a prefix of b
    (all of length k bases) """
    if a[-k:] == b[:k]:
        return k
    else:
        return 0
    
def graphs(reads, readsDict, k):
    """ Given a list of reads and a dictionary (refer to the first function), returns the adjacency list
    (visit rosalind for more information) """
    pairs = []
    for read1, read2 in pmt(reads, 2):
        olen = overlap(read1, read2, k)
        if olen == k:
            pairs.append((readsName(read1, readsDict), readsName(read2, readsDict)))
    for tail, head in pairs:
        print(tail + ' ' + head)

d1, r1 = readFasta('rosalind_grph.txt')        
graphs(r1, d1, 3)


"""
Version 2: I adapted this version from the code given by the Coursera course "Algorithms for DNA sequencing",
as well as the functions used for homework week 3.

"""

def overlap2(a, b, k):     # this function is given by the course
    """ Returns the length (of minimum k bases) of the overlap between read a and read b """
    start = 0
    while True:
        start = a.find(b[:k], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

        
def all_kmers(read, k):
    """ Returns all k-mers of length k of a given read (string) """
    all_kmers = []
    for i in range(len(read) - k + 1):
        all_kmers.append(read[i: i+k])
    return all_kmers
     
    
def graphs2(reads, readsDict, k):   # this function is adapted from the course materials
    """ Returns a list of pairs (or edges) of reads that overlap (at least k bases)"""
    
    pairs = []
    suffixSet = {}
    
    for read in reads:
        kmers = all_kmers(read, k)
        for kmer in kmers:
            if not kmer in suffixSet.keys():
                suffixSet[kmer] = set()
            suffixSet[kmer].add(read)
    
    for read in reads:
        overlap_reads = suffixSet[read[-k:]]
        for each in overlap_reads:
            if each != read:
                if overlap2(read, each, k) > 0:
                    pairs.append((readsName(read, readsDict), readsName(each, readsDict)))
                    
    for tail, head in pairs:
        print(tail + ' ' + head)
        
r2, d2 = readFasta('rosalind_grph.txt')        
graphs2(r2, d2, 3)

