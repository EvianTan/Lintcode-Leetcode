'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for x in num:
            dict[x] = 1
        res = 0
        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x-1
                r = x+1
                while l in dict:
                    del dict[l]
                    l -= 1 
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if res < len:
                    res = len
        return res