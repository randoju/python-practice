#20.   Count the number of times each character appears in a given string


def count_character(text):
    char_count = {}
    for i in text:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

a = input("enter :")
result = count_character(a)
print(result)