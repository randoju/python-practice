lst = [1,3,5,7,11]
lst2= [3,4,6,7,8,13,15]
lst3=[1,2,3,4,7,11]

lst4 =[]
for i in lst:
    if i in lst2:
        lst4.append(i)

common = []
for i in lst3:
    if i in lst4:
        common.append(i)

print(common)

