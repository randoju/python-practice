#26.   Find all the substrings of a given string
string = "abc"
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        print(string[i:j])


