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
        
        # if n > 0:
        #     result = n & (n-1) == 0

        # return result 
    
        # Traditional way
        # Loop Division
        if n <= 0:
            return False

         # 如果 n 是偶數，可以整除為0,能整除就執行n除2的動作
         # 像是數學公式的方法
        while n % 2 ==0:
            # n = n // 2
            n //=2

        return n==1


        
# @lc code=end

