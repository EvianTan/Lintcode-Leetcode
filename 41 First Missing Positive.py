'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or nums==[0]:
            return 1
        elif nums ==[1]:
            return 2
        else:
            res = 0
            large = max(nums)
            for i in xrange(1,large):
                if i not in nums:
                    res = i
                    break
            if res == 0:
                return large+1
            else:
                return res