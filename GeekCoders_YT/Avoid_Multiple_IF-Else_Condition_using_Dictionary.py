def calculator(operator, a, b):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    # Map operator strings to functions
    operations = {
        'add': add,
        'sub': sub,
        'mul': mul,
        'div': div
    }

    # Call the operator function with a and b
    return operations[operator](a, b)


# Example usage
print(calculator('add', 2, 3))  # Output: 5