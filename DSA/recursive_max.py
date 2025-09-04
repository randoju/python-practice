#Write a recursive function to find the maximum number in a list.

def find_max_recursive(lst):
    # Base case: if the list is empty, return None
    if not lst:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0],find_max_recursive(lst[1:]))

# Example usage:
my_list = [3, 8, 12, 10, 5]
max_number = find_max_recursive(my_list)
print("The maximum number in the list is:", max_number)
