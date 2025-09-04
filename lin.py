from collections import *
words = "apple banana apple orange banana apple"

word=words.split()

freq = Counter(word)

print(sorted(freq.items(),key=lambda x:x[1],reverse=True))
