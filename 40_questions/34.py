#34.   Find the second smallest element in a given array of integers.numbers = [3, 8, 2, 7, 5]

# Initialize first_small and second_small with None
first_small = second_small = None

for n in numbers:
    if first_small is None or n < first_small:
        second_small = first_small  # Update second_small before updating first_small
        first_small = n  # Update first_small
    elif (second_small is None or n < second_small) and n != first_small:
        second_small = n  # Update second_small

# Check if we found a valid second_small value
if second_small is not None:
    print("Second smallest element:", second_small)
else:
    print("No second smallest element found")


🔹 Why Did I Use None Here but Not Before?
In the second largest element program, I initialized first_max and second_max with values from the list directly because:

All numbers in the list are expected to be positive or non-empty.

We are looking for the largest numbers, so initializing with the first value is generally safe.

Most edge cases (like duplicates or single elements) still return correct values.

But in the second smallest element program, we need None because:

If all elements are the same, just using numbers[0] for both first_small and second_small will return a wrong value.

If there is only one element, second_small shouldn't be set to that value.

We need a way to check if second_small was updated correctly.

#Should We Use None for the Second Largest Element Program Too?
numbers = [3, 8, 2, 7, 5]

first_max = second_max = None

for num in numbers:
    if first_max is None or num > first_max:
        second_max = first_max
        first_max = num
    elif second_max is None or (num > second_max and num != first_max):
        second_max = num

# Check if we found a valid second_max
if second_max is not None:
    print("Second largest element:", second_max)
else:
    print("No second largest element found")
