p=[[1, 5, 9],
   [3,6,11],
   [4,7,13]]
x = 6

for i in range(len(p)):
    for j in range(len(p[i])):
        if p[i][j]==x:
            print("element found at position",[i,j])

