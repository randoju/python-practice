#2. Create a list of even numbers from a given list of integers.
lst1=[4,5,3,7,5,8,95,3,6,888]
lst2=[]
for i in lst1:
    if i%2==0:
        lst2.append(i)

print(lst2)