'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys
        dp = [sys.maxint]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], dp[i-j**2]+1)
                j += 1
        return dp[-1] 