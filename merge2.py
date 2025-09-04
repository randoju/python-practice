#intervals = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]
intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [1, 4], [4, 5]]
# Sort intervals based on start time
intervals.sort()


prev_start, prev_end = intervals[0]

non_overlapping = []

for start,end in intervals[1:]:
    if start > prev_end:
        non_overlapping.append((prev_start,prev_end))
        prev_start,prev_end = start, end
    else:
        prev_end = max(prev_end,end)
non_overlapping.append((prev_start,prev_end))

print(non_overlapping)

