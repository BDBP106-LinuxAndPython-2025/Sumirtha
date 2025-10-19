sequences=["ATGC", "GGCC","AATT","GCGC"]
at_content=[((seq.count('A') + seq.count('T'))/ len(seq))*100 for seq in sequences]
print(at_content)