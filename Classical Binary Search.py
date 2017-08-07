'''
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Have you met this question in a real interview? Yes
Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

Challenge 
O(logn) time
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        if not A:
            return -1
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left+right) / 2
            if A[mid] > target:
                right = mid
            elif A[mid] < target: 
                left = mid
            else:
                return mid
        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1