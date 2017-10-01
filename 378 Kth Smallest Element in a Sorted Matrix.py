'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        if not matrix:
            return 0
        heap = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            heapq.heappush(heap, (matrix[0][i], 0, i))
        for j in range(k-1):
            curt = heapq.heappop(heap)
            x = curt[1]
            y = curt[2]
            if x+1 < row:
                heapq.heappush(heap, (matrix[x+1][y], x+1, y))
        return heap[0][0]