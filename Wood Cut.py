'''
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

 Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Have you met this question in a real interview? Yes
Example
For L=[232, 124, 456], k=7, return 114.

Challenge 
O(n log Len), where Len is the longest length of the wood.
'''

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
            
        start, end = 1, max(L)
        while start+1 < end:
            mid = (start+end)/2
            pieces = sum([i/mid for i in L])
            if pieces >= k:
                start = mid
            else:
                end = mid
                
        if sum([i/end for i in L]) >= k:
            return end
        else:
            return start