'''
Given two strings, write a method to decide if one is a permutation of the other.
'''
class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        '''
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        f = {}
        for j in B:
            if j not in f:
                f[j] = 1
            else:
                f[j] += 1
        
        return d == f
        '''
        return sorted(A) == sorted(B)