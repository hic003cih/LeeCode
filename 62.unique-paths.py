#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):

    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    #     # m = 3, n = 2
    #     # 從 (0,0) 到 (2,1)
    #     # 你一定要：
    #     # → 往下走 2 次（從 0 到 2）
    #     # → 往右走 1 次（從 0 到 1）
    #     total_moves = m + n - 2
    #     down_moves = m - 1
    #     right_moves = n - 1

    #     return factorial(total_moves) // (factorial(down_moves) * factorial(right_moves))
    
    #     # 使用階乘計算組合數
    #     # 5! = 5 × 4 × 3 × 2 × 1 = 120
    #     # 算出整個階層,速度會很慢
    # def factorial(x):
    #     result = 1
    #     for i in range(2, x+1):
    #         # result = result * i
    #         result *= i 
    #     return result

    # 不真的算出整個階乘,速度更快

        N = m + n - 2
        # 在組合數學中,從 n 個元素中選 k 個，跟選 n-k 個，是一樣的事情。
        # 選較小的去乘會比較快
        k = min(m - 1, n -1)
        result = 1
        for i in range(1, k + 1):
            # 先算每一項
            numerator = N - i + 1
            denominator  = i 
            # 最後再乘起來
            result = result * numerator // denominator 
        return result


# @lc code=end

