#33.  Find the second largest element in a given array of integers.
#first:
numbers = [3, 8, 2, 7, 5]


# Step 1: Initialize first_max and second_max with the first element
first_max = second_max = numbers[0]

# Step 2: Iterate through the list
for num in numbers:
    if num > first_max:
        second_max = first_max  # Update second largest
        first_max = num  # Update largest
    elif num > second_max and num != first_max:
        second_max = num  # Update second largest

# Step 3: Print the second largest element
print("Second largest element:", second_max)

#second
numbers = [3, 8, 2, 7, 5]
first_max = max(numbers[0],numbers[1])
second_max = min(numbers[0],numbers[1])

for num in range(2,len(numbers)):
    if numbers[num] > first_max:
        second_max = first_max
        first_max = numbers[num]
    elif numbers[num] > second_max:
        second_max = numbers[num]

print(second_max)
