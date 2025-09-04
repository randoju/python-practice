

s = "python is very easy and it is op and it is interpreter"

s1=s.split(" ",3)
print(s1)
s2=s.capitalize()
print(s2)
substring='is'
s3=s.count(substring)
print(s3)

print(s.replace("pyThon","java"))

print("/".join(s))

b="adurgas"
print(b.strip('a'))
print(len(b))

print(s.find("is"))
print(s.index("very"))

print(ord('a'))
print(ord('A'))

print(type(s.partition("easy")))

c = "12345"
print(c.isdigit())

c1="1234a"
print(c1.isdigit())

print(c.isalpha())
print(c1.isalpha())

print(c.isalnum())
print(c1.isalnum())

print(list(range(10)))
print(list(range(2,21,3)))

t=(10,20,30,40,50)
print(sum(t,4))

a=10
b=20
c=30
t1 = a,b,c
print(t1)
print(type(t1))

t=(100,200,300)
