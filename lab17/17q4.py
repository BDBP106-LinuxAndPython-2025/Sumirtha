test_dict = {"unknown": [5,7,7,7,7], "is": [6,7,7,7], "Best": [9,9,6,5,5]}
max_unique_key = max(test_dict, key=lambda k: len(set(test_dict[k])))
print(max_unique_key)
