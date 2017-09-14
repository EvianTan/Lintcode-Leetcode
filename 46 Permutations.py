'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if nums is []:
            return [[]]
        result = []
        self.helper(result, [], sorted(nums))
        return result
        
    def helper(self, result, temp, nums):
        if nums == []:
            result += [temp]
        else:
            for i in range(len(nums)):
                self.helper(result, temp+[nums[i]], nums[:i]+nums[i+1:])