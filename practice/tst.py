p = [[1, 5, 9],
     [3, 6, 11],
     [4, 7, 13]]
target = 7
output = []

for i in range(len(p)):         # i = row index
    for j in range(len(p[i])):  # j = column index
        if p[i][j] == target:
            output.append((i, j))

print(output)
