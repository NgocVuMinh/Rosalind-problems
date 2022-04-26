""" 
See more at https://rosalind.info/problems/eval/
PROBLEM
Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
-------------------------------- MY SOLUTION ------------------------------

"""
file = open('rosalind_eval.txt').read().split()
n = int(file[0])
sub = file[1]
gcs = [float(i) for i in file[2:]]
no_of_positions = n - len(sub) + 1

GC_count = 0
for base in sub:
    if base in ['G', 'C']:
        GC_count += 1
AT_count = len(sub) - GC_count

results = []
for gc in gcs:
    times = (((1 - gc)/2)**AT_count)*((gc/2)**GC_count)*no_of_positions
    results.append(round(times, 3))

for result in results:
    print(result, end = ' ')