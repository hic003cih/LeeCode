#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# Simulation Traversal
# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or not matrix[0]:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        # 用第一行matrix[0]的長度去看right要多長
        # Use the length of matrix[0] to determine how long right should be.
        left, right = 0, len(matrix[0]) -1

        while top <= bottom and left <= right:

            # 從左到右
            # From the left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # 最上面一行執行結束,收縮第一行
            # After completing the topmost row, shrink the first row.
            top += 1

            # 從上到下
            # From the top to the bottom
            for i in range(top, bottom + 1):
                # 從最右邊開始
                # Start from the rightmost column
                res.append(matrix[i][right])
            # 最右邊執行結束,收縮最右邊
            # After completing the rightmost column, shrink the rightmost column.
            right -=1

            # 如果還有剩餘的行(Row),遍歷右到左
            # If there are remaining rows, traverse right to left.
            if top <= bottom:
                # range(start, stop, step)
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -=1

            # 如果還有剩餘的列(column),執行下到上
            # If there are remaining columns, traverse bottom to top.
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left +=1 
        
        return res




        
# @lc code=end

