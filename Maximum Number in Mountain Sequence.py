'''
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Have you met this question in a real interview? Yes
Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
'''

class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                end = mid
            else:
                return nums[mid]
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]