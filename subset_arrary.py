arr = [3, 34, 4, 12, 5, 2]
# Given target sum
target_sum = 9

# Initialize a flag to track whether a pair is found
pair_found = False

# Iterate through the array
for i in range(len(arr)):
    # Iterate through the array from the current element to the end
    for j in range(i + 1, len(arr)):
        # Check if the sum of arr[i] and arr[j] equals the target sum
        if arr[i] + arr[j] == target_sum:
            print(arr[i], arr[j])
            break  # Break out of the inner loop if a pair is found
    else:
        # If no pair is found in the inner loop, continue to the next iteration
        continue
    # Break out of the outer loop if a pair is found
    break
else:
    # If the outer loop completes without finding a pair, print "not found"
    print("not found")
