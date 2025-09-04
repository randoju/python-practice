from typing import List

# Input array
nums = [3,2,2,3]
val = 3

# Create an empty list to store elements not equal to val
result = []

# Iterate through the array
for num in nums:
    # If the current element is not equal to val, add it to the result list
    if num != val:
        result.append(num)

# Print the result list containing elements not equal to val
print(result)
