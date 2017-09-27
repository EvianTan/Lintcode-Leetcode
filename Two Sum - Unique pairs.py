'''
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if len(nums) < 2:
            return 0
        count = 0
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        while i < j:
            sum = nums[i] + nums[j]
            if target == sum:
                count += 1
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i+=1
                while i < j and nums[j] == nums[j+1]:
                    j-=1
            elif target < sum:
                j-=1
            else:
                i+=1
        return count