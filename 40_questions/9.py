#9. Create a list of all the anagrams of a given word from a list of words
word_list = ["listen", "silent", "enlist", "inlets", "google", "netsil"]
word = "listen"

words_sorted = sorted(word)
anagram=[]

for i in word_list:
    if sorted(i) == words_sorted:
        anagram.append(i)
print(anagram)