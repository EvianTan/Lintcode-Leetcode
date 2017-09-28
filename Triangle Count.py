'''
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

Have you met this question in a real interview? Yes
Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
'''

class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if len(S) < 3:
            return 0
        S = sorted(S)
        count = 0
        for i in range(len(S)):
            l = 0
            r = i-1
            while l < r:
                if S[l]+S[r] > S[i]:
                    count += r-l
                    r -= 1
                else:
                    l += 1
        return count