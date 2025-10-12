def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper
@log_function_call
def gc_content(dna_sequence):
    dna_sequence = dna_sequence.upper()
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_bases = len(dna_sequence)
    if total_bases == 0:
        return 0.0
    return round((gc_count / total_bases) * 100, 2)
sequence = "ATGCGCGTAC"
print("GC%:", gc_content(sequence))
