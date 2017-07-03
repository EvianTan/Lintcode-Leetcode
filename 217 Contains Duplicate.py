'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        res = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
                if dic[i] == 2:
                    res = 1
        if res == 0:
            return False
        else:
            return True