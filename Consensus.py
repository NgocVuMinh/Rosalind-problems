print("""



""")

#     See more (including information on consensus and profile and sample datasets) at https://rosalind.info/problems/cons/

#     PROBLEM:
#     Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times 
#     that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on.
#     A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds 
#     to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple 
#     possible consensus strings.

#     Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#     Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

#     !!! NOTICE that the actual dataset that Rosalind gives you looks something more like this (so you have to take into account the seperated lines):
#     >Rosalind_1
#     ATCCAGCT
#     GGGCAACT
#___________________________________________________________________________________________________________________________________________

#     MY SOLUTION:

import pandas as pd
import re
pd.set_option("display.max_columns", None)

#----------------Dealing with the file-----------------------
download = open('rosalind_cons5.txt','r').read()
trimread = download.replace('\n','')
split = re.split('>',trimread)
split = split[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)
#------------------------------------------------------------

df = pd.DataFrame()

def split_dna(dna):
    return [base for base in dna]

for i in range(len(file)):
    df[i+1] = split_dna(file[i])
    
df1 = df.transpose()

profile = pd.DataFrame({'base': ["A", "C", "G", "T"], 'e': [0, 0, 0, 0]})
profile.set_index('base', inplace=True)

for k in df1.columns:
    profile['P'+str(k)] = df1[k].value_counts()

profile.drop('e', axis=1, inplace=True)
profile.fillna(0, inplace=True)

con_list = []
for col in profile:
    con_list.append(profile[col].idxmax())
con = ''.join(con_list)

print(con)
print(profile)







print("""



""")