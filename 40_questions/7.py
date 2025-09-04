#7.  Create a list of all the first letters of words in a given sentence.
sentence = "Create a list of all the first letters of words in a given sentence."
sentence2 = sentence.split()
first_letters = []

for i in sentence2:
    first_letters.append(i[0])

print(first_letters)