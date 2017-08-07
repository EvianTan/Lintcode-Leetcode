'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        if nums[start] < nums[end]:
            max = len(nums)-1
        else:
            while start+1 < end:
                mid = (start+end)/2
                if nums[mid] > nums[start]:
                    start = mid
                else:
                    end = mid
            if nums[start] < nums[end]:
                max = end
            else:
                max = start
        
        if nums[0] > target:
            start, end = max, len(nums)-1
        elif nums[0] <= target:
            start, end = 0, max
        
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1