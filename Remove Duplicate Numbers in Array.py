'''
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.

 Notice

You don't need to keep the original order of the integers.

Have you met this question in a real interview? Yes
Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Challenge 
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
'''

class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        dict = {}
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] not in dict:
                dict[nums[i]] = 1
                i += 1
            else:
                if nums[j] not in dict:
                    nums[i] = nums[j]
                    dict[nums[i]] = 1
                    i += 1
                    j -= 1
                else:
                    j -= 1
        return len(dict)