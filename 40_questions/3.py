#3. Create a list of vowels from a given string.
str = "Create a list of vowels from a given string"
vow = ['a', 'e', 'i', 'o', 'u']
lst1 = list(str.lower())

lst2 = [i for i in lst1 if i in vow]
print(lst2)
