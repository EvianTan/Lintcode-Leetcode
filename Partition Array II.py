'''
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.

 Notice

low <= high in all testcases.

Have you met this question in a real interview? Yes
Example
Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.

Change to [1,1,2,3,2,3,4,4].

([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)

Challenge 
Do it in place.
Do it in one pass (one loop).
'''

class Solution:
    """
    @param: nums: an integer array
    @param: low: An integer
    @param: high: An integer
    @return: 
    """
    def partition2(self, nums, low, high):
        # write your code here
        if len(nums) <= 1:
            return
        
        pl, pr = 0, len(nums)-1
        i = 0
        while i <= pr:
            if nums[i] < low:
                nums[pl], nums[i] = nums[i], nums[pl]
                pl += 1
                i += 1
            elif nums[i] > high:
                nums[pr], nums[i] = nums[i], nums[pr]
                pr -= 1
            else:
                i += 1