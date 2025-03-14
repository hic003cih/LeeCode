#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
# Bit Manipulation
# 位移運算（Bitwise Shift <<）
# 一次減去更大的倍數（類似於二分搜尋）
# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 例外處理:避免溢出（當 -2³¹ 除以 -1 時，結果會超過 32-bit 範圍）
        # Handle the special case where the result overflows
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # 確認結果的正負號
        # Determine the sign of the result
        # XOR 運算：只要其中一個是負數，結果就是負數
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # 轉變成絕對值,方便處理
        #Convert dividend and divisor to positive numbers to make the division easier
        dividend = abs(dividend)
        divisor = abs(divisor)

        # 最終商值
        # Initialize the quotient
        quotient = 0

        # 主要邏輯
        # Main division logic
        # 持續找到 dividend 可以減去 divisor 的最大倍數
        while dividend >= divisor:
            # 
            #Initialize temporary divisor and corresponding quotient
            temp, i = divisor, 1

            # 透過位移 (<<) 來找到 divisor 的最大倍數,可以從dividend 減去
            # 將 divisor 乘以 2，再乘以 2，找到最接近 dividend 的倍數
            # Keep doubling temp and i while temp is still less than or equal to dividend
            # 5 = 0000 0101 (二進位)
            # 5 << 1  → 0000 1010  (10)   # 相當於 5 * 2
            # 5 << 2  → 0001 0100  (20)   # 相當於 5 * 4
            # 檢查除數temp最大的兩倍會不會超過被除數,如果不會,繼續指數級增長到找到最大的除數
            while dividend >= (temp << 1):
                # Use << is more efficient than * 2
                # Avoid to use * 2
                # 將 temp 和 i 都乘以 2
                # temp = temp << 1
                temp <<= 1 # Double temp (equivalent to temp * 2)
                # i = i << 1
                i <<= 1 # Double i (equivalent to i * 2)
            # 減去找到的最大值, 並累加商值
            # Subtract temp from dividend and add i to quotient
            # dividend = dividend - temp
            dividend -= temp
            # quotient = quotient + i
            quotient += i
        
        # 如果是負數,要把負號加回去
        #Apply the sign to the result
        return sign * quotient

        
        
# @lc code=end

