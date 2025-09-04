import math
def narcissistic(number):
    num = str(number)
    s = 0
    for i in num:
        s += int(i) ** len(num)  # Use ** instead of math.pow for simplicity
    return s == number  # Check if sum equals the original number

print(narcissistic(1634))
