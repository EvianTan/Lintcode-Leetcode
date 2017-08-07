'''
First Position of Target 

 Description
 Notes
 Testcase
 Judge
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Have you met this question in a real interview? Yes
Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        start, end = 0, len(nums)
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] >= target :
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        elif nums[end] == target :
            return end
        return -1