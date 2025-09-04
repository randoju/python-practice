intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [1, 4], [4, 5]]
intervals.sort()
#[[1, 3], [1, 4], [2, 6], [4, 5], [8, 10], [15, 18
non_overlapping = []

pre_start,pre_end = intervals[0]

for start, end in intervals[1:]:
    if start > pre_end:
        non_overlapping.append((pre_start,pre_end))
        pre_start,pre_end = start, end
    else:
        pre_end = max(pre_end,end)

non_overlapping.append((pre_start,pre_end))
print(non_overlapping)

