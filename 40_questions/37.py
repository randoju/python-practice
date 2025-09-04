#37.   Create a new array from a given array by reversing its elements.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []

for i in numbers[::-1]:
    reversed_numbers.append(i)

print(reversed_numbers)