#39.   Create a new array from a given array by selecting only the elements that are divisible by 3 and 5.
numbers = [1,2,3,4,5,6,7,8,9,10,11]
new=[]
for i in numbers:
    if i%3 ==0 and i%5==0:
        new.append(i)
print(new)