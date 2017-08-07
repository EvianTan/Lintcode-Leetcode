'''
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Have you met this question in a real interview? Yes
Example
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.

Challenge 
Time complexity in O(logn)
'''

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        a = -1
        b = -1
        if not A or (len(A) == 1 and A != [target]):
            return 0
        start, end = 0, len(A)-1
        while start+1 < end:
            mid = (start+end)/2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            a = start
        else:
            a = end
        while a == -1:
            return 0
        start, end = 0, len(A)-1
        while start+1 < end:
            mid = (start+end)/2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            b = end
        else:
            b = start
        return b-a+1