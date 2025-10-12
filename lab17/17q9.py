def extract_codons(sequence, position):
    start = position - 1
    codons = []
    for i in range(start, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        codons.append(codon)

    return codons
dna_sequence = "GTTTCGATTATAACG"
codons_pos1 = extract_codons(dna_sequence, 1)
print("Codons from 1st position:", codons_pos1)
codons_pos3 = extract_codons(dna_sequence, 3)
print("Codons from 3rd position:", codons_pos3)
