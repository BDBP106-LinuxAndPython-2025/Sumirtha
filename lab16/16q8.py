S = input("Enter a sentence: ")
W = input("Enter the word to count: ")
words = []
word = ""
for char in S:
    if char == ' ':
        if word != "":
            words.append(word)
            word = ""
    else:
        word += char
if word != "":
    words.append(word)
count = 0
for w in words:
    if w == W:
        count += 1
print(f"The word '{W}' occurs {count} times in the sentence.")