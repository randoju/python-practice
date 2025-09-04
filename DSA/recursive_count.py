#4.2 Write a recursive function to count the number of items in a list.
def count_items_recursive(lst):
    if not lst:
        return 0
    else:
        return 1 + count_items_recursive(lst[1:])

lst = [1,2,3,4,5]
count = count_items_recursive(lst)
print(count)


