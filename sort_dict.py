#sort based on the value ,if values are same sort based on the keydata = {
data = {
    "d": 3,
    "f": 1,
    "a": 1,
    "c": 2,
    "b": 2,
    "e": 3,
    "h": 2
}

data2 = sorted(data.items(), key=lambda x :(x[1],x[0]))
print(data2)

#[('f', 1), ('a', 1), ('c', 2), ('b', 2), ('h', 2), ('d', 3), ('e', 3)]
#[('a', 1), ('f', 1), ('b', 2), ('c', 2), ('h', 2), ('d', 3), ('e', 3)]