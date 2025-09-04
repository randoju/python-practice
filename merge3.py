# Example 1: [(0, 3), (1, 2)]    output: [(0, 3)]
intervals = [(0, 3), (1, 2)]
intervals.sort()
preS,preE = intervals[0]
non_overlapping = []

for start, end in intervals[1:]:
    if start >preE:
        non_overlapping.append((preS,preS))
        preS,preE=start,end
    else:
        preE=max(preE,end)
non_overlapping.append((preS,preE))
print(non_overlapping)