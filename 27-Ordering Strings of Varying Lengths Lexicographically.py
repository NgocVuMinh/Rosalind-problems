""" 
See more at https://rosalind.info/problems/lexv/
PROBLEM
Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).
Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
-------------------------------- MY SOLUTION ------------------------------

"""
from itertools import product as prod

file = open('rosalind_lexv.txt').read().split()
symbols = file[:-1]
alphabet = dict(zip(symbols, range(len(symbols))))
k = int(file[-1])

m = []
for i in range(len(symbols)):
    for j in range(1, k+1):
        m = m + [''.join(i) for i in prod(symbols, repeat=j)]
m = set(m)
m = sorted(m, key = lambda j: [alphabet[i] for i in j])

for x in m:
    print(x)