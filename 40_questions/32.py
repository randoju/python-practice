#32.   Create an array of all the even numbers from a given array of integers.
numbers = [3, 8, 2, 7, 5]
even=[]
for i in numbers:
    if i %2 ==0:
        even.append(i)

print(even)