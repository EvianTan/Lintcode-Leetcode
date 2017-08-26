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

def _permute(result, x, nums):
            if nums == []:
                result += [x]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    _permute(result, x+[nums[i]], nums[:i]+nums[i+1:])
                    
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        result = []
        _permute(result, [], sorted(nums))
        return result