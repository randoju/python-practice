#arr = [3, 34, 4, 12, 5, 2]
#sum_required = 9
arr = [6, 2, 7, 4, 1, 3, 6]

# Given target sum
sum_required = 12
n = len(arr)
print(n)
lst = []
for i in range(0, n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == sum_required:
            lst.append([arr[i], arr[j]])  # Append elements, not indices
print(lst)
