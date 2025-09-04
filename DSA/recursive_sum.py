#Write out the code for the earlier sum function.
def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0]+sum_recursive(numbers[1:])


numbers = [1, 2, 3, 4, 5]
result = sum_recursive(numbers)
print("The sum is:", result)

