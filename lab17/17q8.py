def interchange_even_odd(lst):
    even_indices = [i for i, val in enumerate(lst) if isinstance(val, int) and val % 2 == 0]
    odd_indices = [i for i, val in enumerate(lst) if isinstance(val, int) and val % 2 != 0]
    even_values = [lst[i] for i in even_indices]
    odd_values = [lst[i] for i in odd_indices]
    for i, idx in enumerate(even_indices):
        if i < len(odd_values):
            lst[idx] = odd_values[i]
    for i, idx in enumerate(odd_indices):
        if i < len(even_values):
            lst[idx] = even_values[i]

    return lst
input_list = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
result = interchange_even_odd(input_list.copy())
print("Result after interchange:", result)
