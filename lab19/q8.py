import random
def protein_energy(temp):
    def calculate_free_energy(enthalpy, entropy):
        return enthalpy - temp * entropy
    use_random = input("Use random values for ΔH and ΔS? (yes/no): ").strip().lower()
    if use_random == "no":
        try:
            enthalpy = float(input("Enter ΔH (in kJ/mol): "))
            entropy = float(input("Enter ΔS (in kJ/mol·K): "))
        except ValueError:
            print("Invalid input. Using random values instead.")
            enthalpy = random.uniform(-100, 100)
            entropy = random.uniform(-1, 1)
    else:
        enthalpy = random.uniform(-100, 100)
        entropy = random.uniform(-1, 1)

    delta_g = calculate_free_energy(enthalpy, entropy)
    print(f"\nΔH = {enthalpy:.2f} kJ/mol")
    print(f"ΔS = {entropy:.4f} kJ/mol·K")
    print(f"T  = {temp} K")
    print(f"ΔG = {delta_g:.2f} kJ/mol")
    return "stable" if delta_g < 0 else "unstable"
temperature = 310
result = protein_energy(temperature)
print("Protein is:", result)
