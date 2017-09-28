'''
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

 Notice

It's guaranteed there is only one available solution

Have you met this question in a real interview? Yes
Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
'''

class Solution:
    """
    @param: nums: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == abs(target):
                    return [i+1, j+1]