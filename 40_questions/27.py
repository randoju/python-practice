#27.   Create a string of all the words in a given sentence in reverse order
sentence = "Python is fun to learn"
reversed = ' '.join(sentence.split()[::-1])
print(reversed)