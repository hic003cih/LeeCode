#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
#  平方乘法法則
# Exponentiation by Squaring
# "分治法"（Divide & Conquer）
# 每次讓n減半
# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 任何數的 0 次方等於 1
        if n ==0: return 1

        # 判斷 n 是否為負數
        neg_exp = n < 0
        # 取絕對值
        n = abs(n)
        result =1.0

        # 2^5 x = 2, n = 5, result = 1
        while n:
            # 用來決定n是否為奇數, & 是and的意思
            # n = 0 -> 0000 & 0001 => 0000
            # n = 1 -> 0001 & 0001 => 0001
            if n & 1:
                # 乘上當前的 x
                # 2 ^ 5 -> 2 ^ 4 * 2 => 所以要乘上一次自己
                # result = 1.0 * 4.0 = 4.0
                result *=x
            # 平方 x，將 n 減半
            # 2.0 * 2.0 = 4.0
            x *= x
            # n 除以 2
            # n = 10 // 2 = 5
            # n = 10 (二進制: 1010)
            # n >>= 1  (右移 1 位)
            # n = 5  (二進制: 0101)
            n >>=1

        # 如果原本是負數指數，則取倒數
        return result if not neg_exp else 1/result


# @lc code=end

