#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle the special case where the result overflows
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        #Convert dividend and divisor to positive numbers to make the division easier
        dividend = abs(dividend)
        divisor = abs(divisor)
        # Initialize the quotient
        quotient = 0

        # Main division logic
        while dividend >= divisor:
            #Initialize temporary divisor and corresponding quotient
            temp, i = divisor, 1

            # Keep doubling temp and i while temp is still less than or equal to dividend
            while dividend >= (temp << 1):
                # Use << is more efficient than * 2
                # Avoid to use * 2
                temp <<= 1 # Double temp (equivalent to temp * 2)
                i <<= 1 # Double i (equivalent to i * 2)
            # Subtract temp from dividend and add i to quotient
            dividend -= temp
            quotient += i
        
        #Apply the sign to the result
        return sign * quotient

        
        
# @lc code=end

