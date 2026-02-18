words = ["apple", "bat", "banana", "cat", "cherry"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)
