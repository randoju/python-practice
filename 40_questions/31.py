#31.   Find the minimum element in a given array of integers.
numbers = [-3, -8, -2, -7, -5]
min_value = numbers[0]  # Initialize with the first element
for i in numbers:
    if i <min_value:
        min_value = i
print(min_value)