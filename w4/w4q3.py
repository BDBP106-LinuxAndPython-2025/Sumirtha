proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]
needed_proteins=[name for name in proteins if name[0]=='H' or name[-3:]=='ase']
print(needed_proteins)