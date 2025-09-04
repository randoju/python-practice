#5. Create a list of all the positive numbers from a given list of integers.
numbers = [-10, 25, -7, 33, 0, -5, 12, 50, -1]  # Example list


positive_list = [i for i in numbers if i>0]
print(positive_list)