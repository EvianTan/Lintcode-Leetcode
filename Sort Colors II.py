'''
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

 Notice

You are not suppose to use the library's sort function for this problem.

k <= n

Have you met this question in a real interview? Yes
Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge 
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
'''

class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        l = 0
        r = len(colors)-1
        i = 0
        min = 1
        max = k
        while min < max:
            while i <= r:
                if colors[i] == min:
                    colors[l], colors[i] = colors[i], colors[l]
                    i += 1
                    l += 1
                elif colors[i] == max:
                    colors[r], colors[i] = colors[i], colors[r]
                    r -= 1
                else:
                    i += 1
            i = l
            min += 1
            max -= 1