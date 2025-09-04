#6. Create a list of all the uppercase characters from a given string.
text = "Create a List of UPPERCASE Characters from a Given String"
upper_chars = [i for i in text if i.isupper()]
print(upper_chars)