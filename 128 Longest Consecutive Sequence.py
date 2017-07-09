'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        dp = [1]*n
        res = 1
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                res += 1
                dp[i] = res
            elif nums[i] == nums[i-1]:
                dp[i] == res
            else:
                res = 1
                dp[i] = 1
        return max(dp)