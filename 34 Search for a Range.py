'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            a = start
        elif nums[end] == target:
            a = end
        else:
            return [-1,-1]
        start, end = a, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            b = end
        else:
            b = start
        return [a,b]