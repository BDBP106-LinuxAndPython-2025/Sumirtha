def cel_to_fah(cel):
    return (cel * 9/5) + 32
cel = [0,45,90]
fah = list(map(cel_to_fah,cel))
print("Fahrenheit values:",fah)