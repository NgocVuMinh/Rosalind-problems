#     See more (including information on consensus and profile and sample datasets) at https://rosalind.info/problems/cons/

#     PROBLEM:
#     Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times 
#     that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on.
#     A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds 
#     to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple 
#     possible consensus strings.

#     Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#     Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

#     !!! NOTICE that the actual dataset that Rosalind gives you is in FASTA format, so it looks something more like this (need to take into account the seperated lines):
#     >Rosalind_1
#     ATCCAGCT
#     GGGCAACT
#____________________________________ MY SOLUTION _______________________________________


import pandas as pd
import re
pd.set_option("display.max_columns", None)                 # displaying all columns since the output dataframe is huge (>900 columns)

fas = open('rosalind_cons5.txt','r').read()                # dealing with the fasta format
trim = fas.replace('\n','')
split = re.split('>',trim)[:1]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)

df = pd.DataFrame()                                        # creating a blank dataframe, then append DNA strings in as rows
def split_dna(dna):
    return [base for base in dna]
for i in range(len(file)):
    df[i+1] = split_dna(file[i])
df1 = df.transpose()

profile = pd.DataFrame({'base': ["A", "C", "G", "T"], 'e': [0, 0, 0, 0]})                # creating the profile
profile.set_index('base', inplace=True)
for k in df1.columns:
    profile['P'+str(k)] = df1[k].value_counts()
profile.drop('e', axis=1, inplace=True)
profile.fillna(0, inplace=True)

con_list = []                                                        # creating the consensus
for col in profile:
    con_list.append(profile[col].idxmax())
con = ''.join(con_list)

print(con)
print(profile)
