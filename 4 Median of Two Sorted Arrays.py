'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n/2+1)
        else:
            return (self.findKth(nums1, nums2, n/2) + self.findKth(nums1, nums2, n/2+1))/2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
        a = A[k/2-1] if len(A) >= k/2 else None
        b = B[k/2-1] if len(B) >= k/2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[k/2:], B, k-k/2)
        return self.findKth(A, B[k/2:], k-k/2)