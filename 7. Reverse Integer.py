# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Constraints:
#
#     -2**31 <= x <= 2**31 - 1
x = -123
if x > 0:
    x = str(x)
    y = int(x[::-1])
else:
    x = x * -1
    x = str(x)
    y = int(x[::-1]) * -1
if -2**31 <= y <= 2**31 - 1:
    print(y)
else:
    print(0)
print(type(y))
