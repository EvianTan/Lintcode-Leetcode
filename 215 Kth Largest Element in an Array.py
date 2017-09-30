'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.helper(nums, 0, len(nums)-1, k)
        
    def helper(self, nums, start, end, k):
        if start == end:
            return nums[start]
        i = start
        j = end
        pivot = nums[(i+j)/2]
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i<= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
        if start+k-1 <= j:
            return self.helper(nums, start, j, k)
        if start+k-1 >= i:
            return self.helper(nums, i, end, k-(i-start))
        return nums[j+1]