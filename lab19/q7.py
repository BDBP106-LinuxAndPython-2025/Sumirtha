def analyse_dna(sequence):
    def gc_content() :
        gc_count=0
        for base in sequence():
            if base == 'g' or base == 'c' or base == 'G' or base == 'C':
               gc_count += 1
            if len(sequence) == 0:
              return 0
gc_percent=(gc_content/len(sequence))*100
if gc_percent > 50:
    print("The DNA sequence is GC rich", gc_percent)
else:
    print("The DNA sequence is AT rich", 100 -gc_percent)

