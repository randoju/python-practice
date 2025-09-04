l2 = []
for i in range(2, 21):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # runs if loop not broken → prime
        l2.append(i)

print(l2)
