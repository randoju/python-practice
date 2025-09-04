a = [1,1,1,2,2,3,4,5]
k=2
def k_most_element(a,k):
    d={}
    s = set()
    for i in a:
        if i in d:
            d[i]+=1
            if d[i]>=k:
                s.add(i)

        else:
            d[i]=1
    return list(s)


print(k_most_element(a,k))