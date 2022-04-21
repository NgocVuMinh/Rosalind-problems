""" 
See more (including information on how to access UniProt database and a sample dataset) at https://rosalind.info/problems/mprt/
PROBLEM
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

-------------------------------- MY SOLUTION ------------------------------

"""

import re
from urllib.request import urlopen


def accessIDs(filename):
    """Given a text file of UniProt access IDs, return a list of those IDs"""
    accessIDs = []
    with open(filename, 'r') as file:
        for ID in file:
            accessIDs.append(ID.strip())
    return accessIDs


def findmotif(accessIDs, motif):
    
    # Get IDs and their corresponding proteins
    allproteins = {}
    for ID in accessIDs:
        link = "https://www.uniprot.org/uniprot/" + ID + ".fasta"
        fasta = urlopen(link).read().decode()
        fasta_split = fasta.strip().split("\n")  # fasta format to a string
        proteins = ''.join(fasta_split[1:]) # skip the first line, the proteins start at line 2
        allproteins[ID] = proteins # return a dict, IDs as keys, proteins as values

    # Using regular expression to search for all matches, return their locations
    results = []
    for ID in allproteins.keys():
        proteins = allproteins[ID]
        matches = re.findall(motif, proteins)
        locs = []
        for match in matches:
            loc = re.search(match, proteins).start()
            locs.append(loc + 1)
        
        # re.findall does not count for overlapping, solve this by iterating over the substring of proteins between the found location
        # e.g: locs = [5, 11, 46], search for the motif again in proteins[5:11] and proteins[11:46]
        for i in range(len(locs)-1): 
            sub = proteins[locs[i]: locs[i+1]]
            if not re.search(motif, sub) is None:
                loc_sub = re.search(motif, sub).start()
                locs.append(loc_sub + 1 + locs[i])       
        results.append((ID, ' '.join(map(str, sorted(locs)))))
    
    for ID, matches in results: # print out the results as how Rosalind requires
        print(*[ID, matches], sep="\n")
        
        
        
motif = "N[^P][ST][^P]"
findmotif(accessIDs("rosalind_mprt.txt"), motif)