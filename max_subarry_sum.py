
# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Initialize variables to track maximum subarray sum and current sum
max_sum = current_sum = 0

# Iterate through the array
for num in nums:
    # Update current sum by choosing between extending the current subarray or starting a new subarray
    current_sum = max(num, current_sum + num)
    # Update maximum subarray sum
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum:", max_sum)
