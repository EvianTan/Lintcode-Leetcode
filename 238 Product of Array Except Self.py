'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        if nums.count(0)>1:
            res = [0]*n
        else:
            multi = 1
            for i in nums:
                if i!=0:
                    multi *=i
            if nums.count(0)==1:
                a = nums.index(0)
                res = [0]*n
                res[a] = multi
            else:
                for i in nums:
                    res.append(multi/i)
        return res