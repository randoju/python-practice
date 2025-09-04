#sort by second element
t1 = [(5,2),(1,9),(3,7),(4,5)]


for i in range(len(t1)):
    for j in range(i + 1, len(t1)):
        if t1[i][1] > t1[j][1]:
            # Swap if second element of t1[i] is greater than that of t1[j]
            temp = t1[i]
            t1[i] = t1[j]
            t1[j] = temp

print(t1)


