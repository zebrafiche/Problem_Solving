"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P     A     H      N
 A  P   L  S  I   I   G
  Y      I     R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

"""

# So number of rows essentially means how many letters will be in a particular line.
# So imagine the letters as their index numbers in the string.
'''
1       5       9           13
  2   4   6   8   10    12      14
    3       7        11
'''

# Then to get the final string we add the letters in a straight line.


