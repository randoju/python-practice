#11. Create a list of all the words that start and end with the same letter from a given list of words using list comprehension.
words = ["level", "hello", "radar", "world", "deed", "python", "noon", "data"]
same_letter_words = []

for word in words:
    if word[0] == word[-1]:
        same_letter_words.append(word)

print(same_letter_words)