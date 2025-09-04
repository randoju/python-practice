#21.   Find the most common character in a given string
text = "banana"
char_count = {}  # Dictionary to store character counts

# Count occurrences of each character
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_common_char = ""
most_common_count = 0
print(char_count)
for key,value in char_count.items():
    if value > most_common_count:
        most_common_char = key
        most_common_count = value

print(f"The most common character is '{most_common_char}' appearing {most_common_count} times.")



