# Define the matrix
m = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
]

# Define the element you want to search for
target = 70

# Iterate through each row of the matrix
for i in range(len(m)):

    # Iterate through each element in the row
    for j in range(len(m[i])):

        # Check if the current element matches the target
        if m[i][j] == target:
            # Print the position of the element
            print(f"Element found at position: ({i}, {j})")
            break
    else:
        # Continue the outer loop if the element was not found in the current row
        continue
    # If the element was found, exit the outer loop
    break
