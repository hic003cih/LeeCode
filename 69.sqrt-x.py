#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x # The square root of 0 or 1 is the number itself
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid ==x:
                return mid
            #If the square of mid is greater than x, search the left half
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right #When the loop ends, 'right' is the floor of the sqrt
        
# @lc code=end

