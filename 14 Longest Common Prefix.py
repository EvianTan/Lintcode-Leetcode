'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        hold, res = zip(*strs), ""
        for i in hold:
            if len(set(i)) > 1: 
                break
            res += i[0]
        return res