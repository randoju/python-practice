#17.   Remove all the whitespace characters from a given string
text = "Hello, How Are You?"
text2 = "".join(text.split())
print(text2)

#2nd approach
text = "Hello, How Are You?"
text_no_spaces = ""  # Initialize an empty string

for char in text:
    if not char.isspace():  # Check if the character is NOT a whitespace
        text_no_spaces += char  # Append non-whitespace characters

print(text_no_spaces)

#3rd approach
text = "Hello   World!  How are  you?"
text_no_spaces = text.replace(" ", "")  # Remove spaces

print(text_no_spaces)

#4th approach
import re

text = "Hello, How Are You?"
text2 = re.findall(r'\b\w+\b', text)  # Extract only words

print(text2)
