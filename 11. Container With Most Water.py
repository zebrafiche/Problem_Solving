'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

'''
1. Find the index of the greatest item in array height. This is the highest bar.
2. For every bar in the plane, find
    1. The distance of the bar from the highest bar, index difference. 
    2. The height of the bar itself.
    3. Multiply 2 to 1 to get the volume of water it will hold. 
    4. Store it in another empty array. 
3. Find the greatest value in the array formed in 2(4).
'''

# height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height2 = [1, 1]
# height3 = [1, 2, 1]

height = [1, 2, 1]

max_volume = 0

fp_index = 0
sp_index = 1


def area(index1, index2, h1, h2):
    b = index2 - index1
    h = min(h1, h2)
    a = b * h
    return a


on = True
while on:
    first_pointer = height[fp_index]
    second_pointer = height[sp_index]
    max_volume = max(max_volume, area(fp_index, sp_index, first_pointer, second_pointer))
    sp_index += 1
    if sp_index >= len(height):
        fp_index += 1
        sp_index = min(fp_index + 1, len(height)-1)
    if fp_index >= len(height):
        on = False

print(max_volume)
