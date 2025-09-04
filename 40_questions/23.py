#23.   Find all the anagrams of a given word from a list of words
word_list = ["listen", "silent", "enlist", "inlets", "google", "netsil"]
word = "listen"
anagram=[]
word_sorted = sorted(word)

for i in word_list:
    if sorted(i) == word_sorted:
        anagram.append(i)

print(anagram)
