#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        result = False
        # If n is a power of 2, its binary representation has only one '1', ex. 1000(8)
        # After subtracting 1 from n, the '1' bit will become '0', and all bits to its right become '1'
        # Therefore, n & (n-1) will be 0. ex. 1000(8) & 0111(7) = 0 

        if n >0:
            result = n & (n-1) ==0
        
        return result
    
        # if n<=0:
        #     return False
        # # This approach repeatedly divides 'n' by 2 until it's no longer evenly divisible by 2.
        # # If 'n' is a power of two, its only prime factor is 2.
        # while (n % 2==0):
        #     #Keep dividing 'n' by 2 using integer division (//)
        #     # Integer division ensures 'n' remains an integer, preventing floating-point issues.
        #     n = n // 2
        # # After the loop, if the original 'n' was a power of two
        # # it will have been reduced exactly to 1.
        # return n==1
    

        
# @lc code=end

