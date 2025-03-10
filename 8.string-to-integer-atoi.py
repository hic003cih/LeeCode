#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 設定最大最小值防止溢出
        # Set the maximum and minimum values to prevent overflow
        INT_MAX = 2**31 - 1 # 2147483647
        INT_MIN = -2**31 # -2147483648

        i, n = 0, len(s)
        # 儲存正負數的符號
        # Store the sign of number
        sign = 1
        result = 0

        # 判斷開頭是否有空格,有的話跳過
        # Check if the string starts with a space; if so, skip it.
        while i < n and s[i] == ' ':
            i +=1

        # 判斷開頭的正負號
        # Determine whether the beginning has a positive or negative sign, then store 1 or -1 in the sign variable.
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i +=1

        # 循環判斷是否為數字
        # Loop through and check if each character is a digit.
        while i < n and s[i].isdigit():
            # 如果是數字則將字轉換乘數字
            # If it is a digital, convert the character to an integer.
            digit = int(s[i])

            # 判斷是否溢出,溢出直接返回最大或最小值
            # If overflow occurs, return INT_MAX or INT_MIN.
            if result > (INT_MAX - digit) //10:
                return INT_MAX if sign == 1 else INT_MIN

            # 當 result = 0 且 digit = 0，結果仍然是 0，不影響最終值。
            # When result = 0 and digit = 0, the result remains 0 and does not affect the final value.
            # 轉換後的結果乘上10以後進位
            # Multiply the converted result by 10 to shift digits.
            result = result * 10 + digit
            i +=1

        #最後乘上sign(正負號),轉換成原本的正負號
        # Multiply by sign to restore the original positive or negative value.
        return result * sign
# @lc code=end

