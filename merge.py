intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [1, 4], [4, 5]]

# Sort the intervals by the start time
intervals.sort(key=lambda x: x[0])
print(intervals)


# Initialize a list for the merged intervals
merged_intervals = []

# Initialize the first interval to compare
start, end = intervals[0]

# Iterate through the sorted intervals
for i in range(1, len(intervals)):
    current_start, current_end = intervals[i]
    print(current_end)


    # Check if there is an overlap between the current and previous intervals
    if current_start <= end:
        # Merge the intervals by updating the end time
        end = max(end, current_end)
    else:
        # If there is no overlap, add the current merged interval to the list
        merged_intervals.append([start, end])
        # Update the current interval for the next iteration
        start, end = current_start, current_end

# Add the last merged interval to the list
merged_intervals.append([start, end])

# Print the merged intervals
print(merged_intervals)
