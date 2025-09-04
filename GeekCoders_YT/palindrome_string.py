#CHECK IF A STRING IS PALINDROME OR NOT | DATA ENGINEER | TOP MOST PYTHON INTERVIEW QUESTION SERIES

s = 'sagas'

l = len(s)
c=0

for i in range(l):
    if s[i] != s[l-i-1]:
        c = 1
        break

if c==0:
    print("its palindrome")
else:
    print("not palindorm")

