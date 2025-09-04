#FIND A NON - NEGATIVE INTEGER THAT IS NOT IN THE ARRAY | TOP MOST PYTHON INTERVIEW QUESTION SERIES
#smallest missing positive integer Python interview question

#https://www.youtube.com/watch?v=8g78yfzMlao&ab_channel=NeetCode

#best method
l = [0, 1, 2, 3, 4, 5,7, 8, 9]

d ={}

for i in l:
    d[i]=True

for i in range(len(l)+1):
    if i not in d:
        print(i)
        break

####second methond
arr = [0, 1, 2, 3, 4, 5, 7, 8, 9]
n = len(arr)

# Mark presence by adding a large value to avoid overlap
for i in range(n):
    index = arr[i]
    if index < n:
        arr[index] = arr[index] + n + 1



# Find the first missing non-negative integer
for i in range(n):
    if arr[i] <= n:
        print(i)
        break
else:
    print(n)