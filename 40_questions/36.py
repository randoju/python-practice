#36.   Create a new array from a given array by removing all the duplicates.
numbers = [1, 3, 5, 3, 7, 1, 9, 5]
unique_numbers = []

for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print(unique_numbers)