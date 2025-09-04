#35.   Create a new array from two given arrays by alternating their elements.
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 10, 12]

result = []
len1,len2 = len(arr1),len(arr2)
for i in range(min(len1,len2)):
    result.append(arr1[i])
    result.append(arr2[i])
print(result)
result.extend(arr1[i+1:] or arr2[i+1:])
print(result)