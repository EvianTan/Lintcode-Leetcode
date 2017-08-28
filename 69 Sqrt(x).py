'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start+1 < end:
            mid = (start+end)/2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid
            else:
                end = mid
        if end*end <= x:
            return end
        return start