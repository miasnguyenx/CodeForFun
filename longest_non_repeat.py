"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
str = 'pwwkew'

def longest_non_repeat_v1(string):
    """
    Find the length of the longest substring
    without repeating characters.
    """
    if string is None:
        return 0
    dict = {}
    max_length = 0 #length of string
    j = 0 #begin of string index
    
    for i in range(len(string)):
        if string[i] in dict:
            j = max(dict[string[i]], j)
            print("j = ",j)
        dict[string[i]] = i + 1
        print("dict[" + string[i] + "] = ", dict[string[i]])
        max_length = max(max_length, i - j + 1)
        print("max_length = ", max_length , "\n")
    return max_length

print(longest_non_repeat_v1(str))


    