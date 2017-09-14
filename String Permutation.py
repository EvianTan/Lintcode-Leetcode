'''
Given two strings, write a method to decide if one is a permutation of the other.
'''
class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        if len(A) != len(B):
            return False
        dic1 = {}
        for i in A:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        dic2 = {}
        for j in B:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
        return dic1 == dic2