'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        p = 'I'
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  
        for i in s[::-1]:
            if dic[i] < dic[p]:
                res = res - dic[i]
            else:
                res = res + dic[i]
            p = i
        return res