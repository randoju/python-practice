# Define the list of intervals
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda x: (x[0], x[1]))
# Step 2: Merge overlapping intervals
merged_intervals = []
for interval in intervals:
    if not merged_intervals:
        # If the list of merged intervals is empty, add the current interval
        merged_intervals.append(interval)
    else:
        # Check for overlap with the last merged interval
        last_interval = merged_intervals[-1]
        if last_interval[1] < interval[0]:
            # If there is no overlap, add the current interval
            merged_intervals.append(interval)
        else:
            # If there is overlap, merge the current interval with the last one
            merged_intervals[-1][1] = max(last_interval[1], interval[1])

# Output the merged intervals
print("Merged intervals:", merged_intervals)
