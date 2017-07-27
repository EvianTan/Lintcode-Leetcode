'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        while not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for x in range(n)] for x in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i==0 and j>0:
                        dp[i][j]=dp[i][j-1]
                    elif j==0 and i>0:
                        dp[i][j]=dp[i-1][j]
                    elif i>0 and j>0:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]