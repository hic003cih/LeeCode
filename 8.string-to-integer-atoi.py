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

        INT_MAX = 2**31 - 1 # 2147483647
        INT_MIN = -2**31 # -2147483648

        i, n = 0, len(s)
        sign = 1
        result = 0

        # 忽略前導空白
        while i < n and s[i] == ' ':
            i +=1

        # 判斷正負號
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i +=1

        # 循環判斷是否為數字
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (INT_MAX - digit) //10:
                return INT_MAX if sign == 1 else INT_MIN

            # 當 result = 0 且 digit = 0，結果仍然是 0，不影響最終值。
            result = result * 10 + digit
            i +=1

        return result * sign
# @lc code=end

