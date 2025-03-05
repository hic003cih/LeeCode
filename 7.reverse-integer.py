#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign =-1 if x < 0 else 1
        x = abs(x)

        rev=0

        while x!=0:
            # x=123 digit = 3
            digit = x % 10
            
            x //=10

            if rev > (INT_MAX - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev




        # sign = -1 if x < 0 else 1
        # x = abs(x)

        # rev = 0
        # while x != 0:
        # # x = 123
        # # digit = x % 10  # 取出最後一位數
        # # print(digit)    # 3
        #     digit = x % 10
        # # x = 123
        # # x //= 10  # 移除最後一位數
        # # print(x)  # 12
        #     x //= 10

        #     if rev > (INT_MAX - digit) // 10:
        #         return 0
            
        #     # x = 321
        #     rev = rev * 10 + digit
        # # 恢復原本的正負號
        # return sign * rev

# @lc code=end

