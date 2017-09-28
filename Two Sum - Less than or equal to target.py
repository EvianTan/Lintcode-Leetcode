'''
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given nums = [2, 7, 11, 15], target = 24. 
Return 5. 
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
'''

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if len(nums) < 2:
            return 0
        count = 0
        nums = sorted(nums)
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] <= target:
                count += (r-l)
                l += 1
            else:
                r -= 1
        return count