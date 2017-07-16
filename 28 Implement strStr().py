'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if haystack is None or needle is None:
            return -1
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
            else: 
                return i
        return -1