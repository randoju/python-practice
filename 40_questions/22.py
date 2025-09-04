#22.   Capitalize the first letter of each word in a given string
text = "hello world! this is python."
capitalized_words = []  # Empty list to store capitalized words

for i in text.split():
    capitalized_words.append(i.capitalize())  # Capitalize and store each word



print(capitalized_words)

captalized_text = " ".join(capitalized_words)
print(captalized_text)