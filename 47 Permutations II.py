'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution(object):
    def permuteUnique(self, nums):
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
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.helper(result, temp+[nums[i]], nums[:i]+nums[i+1:])