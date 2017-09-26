'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

 Notice

There is at least one subarray that it's sum equals to zero.

Have you met this question in a real interview? Yes
Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
                                      and the index of the last number
    """
    def subarraySum(self, A):
        dict= {0:-1}
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            if sum in dict:
                return [dict[sum]+1, i]
            dict[sum] = i
        return
