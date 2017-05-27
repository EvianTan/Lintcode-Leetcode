'''

Unique Characters

Implement an algorithm to determine if a string has all unique characters.

Example
Given "abc", return true.
Given "aab", return false.

Challenge 
What if you can not use additional data structures?

'''

def isUnique(str):
    # write your code here
    d = {}
    for i in str:
        if i not in d:
            d[i] = 1
        else:
            return False
    return True

print isUnique("abc")
print isUnique("aab")

'''
cannot use additional data structure

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        l = len(str)
        for i in range(l):
            for j in range(i+1, l):
                if str[i] == str[j]:
                    return False
        return True
'''