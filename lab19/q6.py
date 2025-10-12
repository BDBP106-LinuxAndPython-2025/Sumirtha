def cell_metabolism(glucose_molecules, oxygen_molecules):
    def energy_output(glucose, oxygen):
        possible_reactions = min(glucose, oxygen // 6)
        return possible_reactions * 38
    total_atp = energy_output(glucose_molecules, oxygen_molecules)
    return total_atp
glucose = 5
oxygen = 32
print("Total ATP produced:", cell_metabolism(glucose, oxygen))