'''
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

 Notice

You are not necessary to keep the original order of positive integers or negative integers.

Have you met this question in a real interview? Yes
Example
Given [-1, -2, -3, 4, 5, 6], after re-range, it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

Challenge 
Do it in-place and without extra memory.
'''

class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def rerange(self, A):
        # write your code here
        if not A:
            return
        posNum = 0
        for num in A:
            if num > 0:
                posNum += 1
        posP = 1
        negP = 0
        if posNum*2 > len(A):
            posP = 0
            negP = 1
        while posP < len(A) and negP < len(A):
            while posP < len(A) and A[posP] > 0:
                posP += 2
            while negP < len(A) and A[negP] < 0:
                negP += 2

            if posP < len(A) and negP < len(A):
                temp = A[posP]
                A[posP] = A[negP]
                A[negP] = temp