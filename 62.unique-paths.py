#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):

    # 使用階乘計算組合數
    def factorial(x):
        result = 1
        for i in range(2, x+1):
            result *= i 
        return result
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total_moves = m + n - 2
        down_moves = m - 1
        right_moves = n - 1

        return factorial(total_moves) // (factorial(down_moves) * factorial(right_moves))
    
        

# @lc code=end

