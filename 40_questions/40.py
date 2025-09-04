#40.   Find the intersection of two given lists.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

intersection = []

for i in list1:
    if i in list2:
        intersection.append(i)

print(intersection)