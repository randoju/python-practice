#25.   Find the longest palindrome in a given string


text = "babad"
longest = ""

for i in range(len(text)):
    for j in range(i, len(text)):
        substr = text[i:j+1]
        if substr == substr[::-1] and len(substr) > len(longest):
            longest = substr

print("Longest palindrome:", longest)


# text = "babad"  # You can change this to test with other strings
# longest_palindrome = ""
#
# for i in range(len(text)):
#     # Check for odd-length palindromes (single character center)
#     left, right = i, i
#     while left >= 0 and right < len(text) and text[left] == text[right]:
#         if right - left + 1 > len(longest_palindrome):
#             longest_palindrome = text[left:right+1]
#         left -= 1
#         right += 1
#
#     # Check for even-length palindromes (two adjacent character center)
#     left, right = i, i + 1
#     while left >= 0 and right < len(text) and text[left] == text[right]:
#         if right - left + 1 > len(longest_palindrome):
#             longest_palindrome = text[left:right+1]
#         left -= 1
#         right += 1
#
# print("Longest Palindrome:", longest_palindrome)

