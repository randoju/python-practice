# Python Implementation
students = [(1, "Abbot"), (2, "Doris"), (3, "Emerson"), (4, "Green"), (5, "Jeames")]

# Extract IDs and student names separately
ids = [s[0] for s in students]

names = [s[1] for s in students]


# Swap student names for consecutive pairs
for i in range(0, len(names) - 1,2):
    names[i], names[i + 1] = names[i + 1], names[i]


# Combine IDs and swapped student names back
swapped_students = list(zip(ids, names))

# Print result
print("Final Swapped Seats:")
print(swapped_students)