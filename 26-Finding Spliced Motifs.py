""" 
See more at https://rosalind.info/problems/sseq/
PROBLEM
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
-------------------------------- MY SOLUTION ------------------------------

"""
fasta = open('rosalind_sseq.txt').read()
trim = fasta.replace('\n','')
split = re.split('>',trim)[1:]
file = []
for strand in split:
    strand = strand[13:]
    file.append(strand)
seq = file[0]
subseq = file[1]

def indices(seq, subseq):
    pos = seq.find(subseq[0])
    all_pos = [pos]
    i = 1
    while i < len(subseq):
        pos = seq[all_pos[i-1] + 1:].find(subseq[i]) 
        all_pos.append(pos + all_pos[i-1] + 1)
        i += 1
    for k in range(len(all_pos)):
        all_pos[k] = all_pos[k] + 1
        print(all_pos[k], end=' ')

indices(seq, subseq)