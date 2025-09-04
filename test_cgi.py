# Input: [1, [2, [3, 4], 5], 6]
# Output: [1, 2, 3, 4, 5, 6]

lst = [1, [2, [3, 4], 5], 6]

lst2 = []

def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            lst2.append(i)

flatten(lst)

print(lst2)