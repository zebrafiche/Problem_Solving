"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


strs = ["acc","aaa","aaba"]

def match_word(word1, word2):
    if word1 != word2:
        return False
    else:
        return True


# 1. Make two words the same size
# target_word_length = len(min([word3, word4], key=len))
# word3 = word3[0:target_word_length]
# word4 = word4[0:target_word_length]

# 2. Make a logic so that when two words are not equal, the words are shortened
# while not match_word('flower', 'flowen'):
#     word1 = word1[:-1]
#     word2 = word2[:-1]
# print(word1)

# 3. Loop it over the list of words
word1 = strs[0]
print(word1)
for word in strs[1:]:
    word2 = word
    target_word_length = len(min([word1, word2], key=len))
    word1 = word1[0:target_word_length]
    word2 = word2[0:target_word_length]
    while not match_word(word1, word2):
        word2 = word2[:-1]
        word1 = word1[:-1]
print(word1)


