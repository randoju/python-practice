# Given sequence
s = [6, 2, 7, 4, 1, 3, 6]
# Given target sum
target_sum = 12
# Flag to indicate if the subsequence is found
found = False
# Iterate over each starting index of the sequence
for i in range(len(s)):
    # Initialize the current sum as 0
    current_sum = s[i]
    # Iterate from the starting index to the end of the sequence
    for j in range(i + 1, len(s)):
        # Add the current element to the current sum
        current_sum += s[j]

        # Check if the current sum is equal to the target sum
        if current_sum == target_sum:
            # If found, print the contiguous subsequence
            print("Contiguous subsequence found:", s[i:j+1])
            # Set the flag to True indicating the subsequence is found
            found = True
            # Break the inner loop as we found the subsequence
            break

    # If subsequence is found, break the outer loop
    if found:
        break

# If the flag is still False, print not found
if not found:
    print("Contiguous subsequence not found")
#Ans :Contiguous subsequence found: [7, 4, 1]