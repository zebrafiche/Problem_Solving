"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


def is_palindrome(string):
    if string == string[::-1]:
        return True


s = 'racecardib'

lengths = []
for z in range(len(s)-1, 0, -1):
    # for i in range(0, len(s)):
    #     chunk = s[i:z+1]
    #     # print(chunk)
    #     if is_palindrome(chunk):
    #          # print(chunk)
    #         lengths.append(chunk)

    lengths.extend(s[i:z+1] for i in range(0, len(s)) if is_palindrome(s[i:z+1]))

# print(lengths)

if len(lengths) == 0:
    lengths.append(s)

print(max(lengths, key=len))

