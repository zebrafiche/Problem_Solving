# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


l1 = [2, 4, 3]
l2 = [5, 6, 4]


def reverse_number(list_):
    reversed_num = ''
    for i in reversed(list_):
        reversed_num += str(i)
    return int(reversed_num)


sum_of_two = reverse_number(l1) + reverse_number(l2)
new_string = str(sum_of_two)
new_string_list = []
for k in new_string:
    new_string_list.append(k)
print(new_string_list)


print(reverse_number(new_string_list))