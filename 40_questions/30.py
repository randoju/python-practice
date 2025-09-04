#30.   Find the maximum element in a given array of integers.
numbers = [-2, -8, -3, -7, -5]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i

print(max)