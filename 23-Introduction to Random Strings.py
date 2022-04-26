""" 
See more at https://rosalind.info/problems/prob/
PROBLEM
Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
-------------------------------- MY SOLUTION ------------------------------

"""
from math import log10 as log

file = open('rosalind_prob.txt').read().split()
DNA = file[0]
gc_contents = [float(i) for i in file[1:]]

countAT = 0
countGC = 0
for base in DNA:
    if base in ['A', 'T']:
        countAT += 1
    else:
        countGC += 1
    
all_logprob = []
for i in gc_contents:
    logprob = log(((1-i)/2)**countAT*(i/2)**countGC)
    all_logprob.append(round(logprob, 3))

for m in all_logprob:
    print(m, end=' ')