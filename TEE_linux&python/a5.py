#Given list of DNA sequence
dna=["ATGCGT","TTTTTT","GCATCC","ATGCAT","CCGGA"]
#list comprehension for sequence starting with ATG
needed_dna=[seq for seq in dna if seq[0:3]=='ATG']
print(needed_dna)