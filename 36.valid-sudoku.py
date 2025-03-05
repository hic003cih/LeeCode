#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in ragne(9):
                num = board[r][c]

                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c//3)

                if (num in rows[r]) or (num in cols[c]) or (num in boxes[box_index]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
            
        return True

        
# @lc code=end

