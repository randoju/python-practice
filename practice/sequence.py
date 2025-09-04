s = [6, 2, 7, 4, 1, 3, 6]
# Given target sum
target_sum = 12


for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if sum(s[i:j]) == target_sum:
            print("Continuous sequence is", s[i:j])

