'''
Given a string and an offset, rotate string by offset. (rotate from left to right)

Have you met this question in a real interview? Yes
Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
Challenge 
Rotate in-place with O(1) extra memory.
'''

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
     def rotateString(self, s, offset):
        if not s:
            return s
        offset %= len(s)
        for x in range(offset):
            temp = s[len(s)-1]
            for i in range(len(s)-1, 0, -1):
                s[i] = s[i-1]
            s[0] = temp