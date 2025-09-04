#8. Create a list of all the unique words from a given sentence
sentence = "Create a list of all all the unique words from a given sentence with unique words"
word_count = {}
lst2=[]
for word in sentence.split():
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1
print(word_count)

for key,value in word_count.items():
    if value == 1:
        lst2.append(key)

print(lst2)

