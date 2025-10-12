from functools import reduce
words = ["Python", "is", "a", "powerful", "programming", "language"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("Sentence:", sentence)