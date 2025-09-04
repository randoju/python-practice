lst = [1, 2, 3, 4, -1, -2, -5,-3, 0]
out = []

for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):  # Start j from i+1
        if lst[i] + lst[j] == 0:
            out.append((lst[i], lst[j]))

print(out)