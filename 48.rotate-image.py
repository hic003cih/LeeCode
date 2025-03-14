#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # 計算長度
        n = len(matrix)

        # 先做轉置,把行跟列對調
        # First, transpose the matrix to swap rows and columns
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 在做水平反轉
        # Then, reverse the matrix horizontally
        for i in range(n):
            matrix[i].reverse()
        
        


        
# @lc code=end

