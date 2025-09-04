#sort based on the value ,if values are same sort based on the keydata = {
data = {
    "d": 3,
    "f": 1,
    "a": 1,
    "c": 2,
    "b": 2,
    "e": 3,
    "h": 2
}

temp = []

# Step 1: Swap to (value, key) for sorting
for key, value in sorted(data.items()):
    temp.append((value, key))

# Step 2: Sort by value, then key, then swap back
dic2 = []
for v, k in sorted(temp):
    dic2.append((k, v))

# Step 3: Convert list of tuples to dictionary
final_dict = dict(dic2)

print(final_dict)
# we can do uisng map and lambda
#dict2 = sorted(data.items(), key=lambda x: (x[1], x[0]))
#print(dict2)

