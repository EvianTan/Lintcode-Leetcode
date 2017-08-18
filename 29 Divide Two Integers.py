'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend == 0:
            return 0
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        a = divisor
        count = 0
        while dividend >= a:
            count += 1
            hold = 0
            while divisor*2 <= dividend:
                divisor *= 2
                hold += 1
                count += 2**(hold-1)
            dividend -= divisor
            divisor = a
        if count*sign > 2147483647 or count*sign < -2147483648:
            return 2147483647
        else:
            return count*sign