""" 
See more at https://rosalind.info/problems/rstr/
PROBLEM
Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
-------------------------------- MY SOLUTION ------------------------------

"""
file = open('rosalind_rstr.txt').read().split()
n = int(file[0])
x = float(file[1])
DNA = file[2]

countAT = 0
countGC = 0
for base in DNA:
    if base in ['A', 'T']:
        countAT += 1
    else:
        countGC += 1
    
prob = 1 - (1 - ((1-x)/2)**countAT*(x/2)**countGC)**n
round(prob, 3)