#24.   Create a string of all the unique characters in a given string
text = "hello world"
unique_chars = ""

for i in text:
    if i not in unique_chars:
        unique_chars += i
print(unique_chars)