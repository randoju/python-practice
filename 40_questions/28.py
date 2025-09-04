#28.   Create an array of integers from a given list of integers.
import array as ar


# Given list of integers
num_list = [1, 2, 3, 4, 5]

# Creating an array of integers
int_array = ar.array('i',num_list)

print(type(int_array))
