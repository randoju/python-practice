def check_sorted(n):
    return all(n[i]<=n[i+1] for i in range(len(n)-1))

print(check_sorted([1,3,2,5,4]))