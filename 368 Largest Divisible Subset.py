'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [1] * n
        father = [-1] * n
        nums.sort()
        m, index = 0, -1
        for i in xrange(n):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        father[i] = j
            if dp[i] >= m:
                m = dp[i]
                index = i
        result = []
        for i in xrange(m):
            result.append(nums[index])
            index = father[index]
        return result