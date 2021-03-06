'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False     
        m = len(matrix)
        n = len(matrix[0])           
        hold = []
        for i in range(m):
            hold += matrix[i]
        start, end = 0, m*n-1
        while start+1 < end:
            mid = (start+end)/2
            if hold[mid] > target:
                end = mid
            elif hold[mid] < target:
                start = mid
            else:
                return True
        if hold[start] == target:
            return True
        if hold[end] == target:
            return True
        return False