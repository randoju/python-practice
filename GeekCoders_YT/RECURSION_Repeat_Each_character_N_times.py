# s="Hello"
# s1=""
# for i in s:
#     s1= s1+i*3
#
# print(s1)

def multiple_string(s,n):
    if len(s)==0:
        return ""
    return s[0]*n+multiple_string(s[1:],n)

print(multiple_string("Hello",3))