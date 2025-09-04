
#target = 7

def find_element_early_stop(matrix,target):
    for row in matrix:
        for col in range(len(row)):
            if row[col] > target:
                break
            if row[col] == target:
                return True, (matrix.index(row),col)
    return False, None
p = [[1, 5, 9],
     [3,6,11],
     [4,7,13]]
target = 7
f = find_element_early_stop(p,target)

print(f)

