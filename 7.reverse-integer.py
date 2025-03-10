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
        # 32位元最大正整數 (INT_MAX) = 2³¹ - 1 = 2147483647
        # The maximum positive integer for a 32-bit system (INT_MAX)  is 2³¹ - 1 = 2147483647
        INT_MAX = 2**31 - 1
        # 32位元最小負整數 (INT_MIN) = -2³¹ = -2147483648
        # The minimum negative integer for a 32-bit system (INT)MIX is -2³¹ = -2147483648
        INT_MIN = -2**31

        # 用-1和1來做最後正負號的變化,如果 x < 0, 則 sign = -1, 否則 sign = 1
        # The sign is determined using -1 and 1: if x < 0, then sign =-1; otherwise, sign = 1
        sign =-1 if x < 0 else 1
        # 先將x轉變成絕對值
        # Convert x to its absolute value first.
        x = abs(x)

        # 用來存轉變後的值
        # Used to store the converted value.
        rev=0

        # 當x 還不為0時, 對每個位數進行反轉
        # While x is not zero, reverse each digit.
        while x!=0:
            # 先取出個位數用來轉換,將個位數放到rev變數中的最開頭
            # First, extract the last digit for conversion and place it at the beginning of the rev variable.
            # x=123 digit = 3
            digit = x % 10
            
            # 將x的值去除個位數後留下
            # Remove the last digit from x and keep the remaining value in x.
            # ex x=123 // 10 -> x = 12
            x //=10

            # 檢查正數是否溢出
            # Check if the positive number overflows
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
            # 檢查負數是否溢出
            # Check if the negative number overflows
            if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < -8):
                return 0
            
            # 先將個位數放到rev中,然後後面的位數在依序放在最後面,個位數往前一個位數,用乘上10了往前一個位數
            # Place the last digit into rev, then append the remaining digits sequentially
            # Shift digits forward by multiplying rev by 10 before adding the next digit
            rev = rev * 10 + digit

        # 最後乘上存在sign中的正負號來恢復原本正副值
        # Restore the original sign by multiplying with 'sign'. 
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

