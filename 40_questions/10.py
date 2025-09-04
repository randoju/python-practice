#10. Create a list of all the permutations of a given string using list comprehension.
from itertools import permutations

word = "abc"
permutation_list = []

for p in permutations(word):
    permutation_list.append("".join(p))

print(permutation_list)
