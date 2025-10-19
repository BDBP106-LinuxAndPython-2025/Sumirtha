def enzyme_activity(name, subs_conc):
    def michaelis_menten(Vmax, Km):
        return (Vmax * subs_conc) / (Km + subs_conc)
    enzyme_data = {
        "Hexokinase": (100, 50),
        "Amylase": (80, 30),
        "Lactase": (120, 60),
        "Catalase": (200, 100)
    }
    if name in enzyme_data:
        Vmax, Km = enzyme_data[name]
        return michaelis_menten(Vmax, Km)
    else:
        return f"Enzyme '{name}' not found in database."
if __name__ == "__main__":
    enzyme_name = "Hexokinase"
    substrate_concentration = 40
    rate = enzyme_activity(enzyme_name, substrate_concentration)
    print(f"Reaction rate for {enzyme_name} at [S] = {substrate_concentration} µM: {rate}")