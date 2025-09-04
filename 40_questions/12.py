#12.   Create a list of all the numbers that are divisible by 3 and 5 from a given list of integers using list comprehension.
numbers = [10, 15, 30, 22, 45, 60, 77, 90, 100, 105]
divisible_3_5 = [num for num in numbers if num %3 == 0 and num  % 5 == 0]
print(divisible_3_5)