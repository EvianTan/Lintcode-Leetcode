'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    '''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        nums.sort()
        if len(nums) <3:
            return None
        res = sys.maxint
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:                    
                sum = nums[l]+nums[r]+nums[i]
                if abs(sum-target) < abs(res-target):
                    res = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        return res