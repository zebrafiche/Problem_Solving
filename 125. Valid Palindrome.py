'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

s = "0P"

# 1. remove all the alphanumerics
s1 = ''
for letter in s:
    if letter.isalnum():
        # 2. turn all the letters into lowercase
        to_add = letter.lower()
        s1 = s1 + to_add
print(s1)
# 3. create a reversed string
s2 = s1[::-1]
print(s2)
# 4. check if the two are the same or not

if s1 == s2:
    print('palindrome')
else:
    print('not a palindrome')
