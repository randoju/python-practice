#15.   Remove all the vowels from a given string
vow = ['a','e','i','o','u']
text = "Hello, World!"
result =''

for i in text:
    if i not in vow:
        result +=i

print(result)