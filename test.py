sent = 'He live in hyderabad'
l = []
for i in sent.split():
    j = len(i)
    if j % 2 == 0:
        l.append(i)

print(max(l))
