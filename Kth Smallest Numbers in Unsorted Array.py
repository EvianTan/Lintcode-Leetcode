'''
Find the kth smallest numbers in an unsorted integer array.

Have you met this question in a real interview? Yes
Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

Challenge 
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
'''

class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    def kthSmallest(self, k, nums):
        # Write your code here
        if k > len(nums) or len(nums) == 0 or k == 0:
            return []
        return self.quickSelect(nums, 0, len(nums)-1, k-1)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        i = start
        j = end
        pivot = nums[(i+j)/2]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
        if j >= k and start <= j:
            return self.quickSelect(nums, start, j, k)
        elif i <= k and end >= i:
            return self.quickSelect(nums, i, end, k)
        else:
            return nums[k]