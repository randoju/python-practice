input_str = "Hello Geeks"
new = []
for i in input_str.split():
    new.append(i[0].upper() + i[1:-1] + i[-1].upper())

print(" ".join(new))