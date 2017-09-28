'''
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)

Challenge 
Do it in O(1) extra space and O(nlogn) time.
'''

class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return 0
        count = 0
        nums = sorted(nums)
        count = 0
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] > target:
                count += (r-l)
                r -= 1
            else:
                l += 1
        return count
            