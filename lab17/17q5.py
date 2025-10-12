def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return ' '.join(result)
sentence = "This is is a test test sentence with with duplicates duplicates"
clean_sentence = remove_duplicate_words(sentence)
print(clean_sentence)
