'''
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Have you met this question in a real interview? Yes
Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

Challenge 
Do it in O(nlogn) time complexity.
'''

class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    import sys
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        i = 0
        j = len(nums)-1
        diff = sys.maxint
        while i < j:
            if nums[i]+nums[j] < target:
                diff = min(diff, target-nums[i]-nums[j])
                i += 1
            elif nums[i]+nums[j] > target:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1
            else:
                return 0
        return diff