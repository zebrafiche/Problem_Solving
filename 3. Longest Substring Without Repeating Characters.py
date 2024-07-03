# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

u = ""
u_list = []
for i in s:
    if i not in u:
        u = u + i
    else:
        u_list.append(u)
        ind = u.index(i)
        u = u[ind+1:]
        u = u + i
u_list.append(u)
# return len(max(u_list, key=len))
print(len(max(u_list, key=len)))

