#18.   Create a string of all the characters in a given list of strings
words = ["Hello", "World", "Python"]
result = ""

for word in words:
    for w in word:
        result += w
print(result)