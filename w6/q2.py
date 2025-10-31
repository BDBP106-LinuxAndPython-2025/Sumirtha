import re
# DNA sequence
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
# Extract all occurrences of "ATACG"
pattern = r"ATACG"
matches = re.findall(pattern, dna)
print(f"Pattern 'ATACG': {matches}")