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

        # Using set to store the number in each row, column, and box
        # 也可以用defaultdict(set)
        # 存放每一行的數字
        # Store the numbers in each row.
        rows = [set() for _ in range(9)]
        # 存放每一列的數字
        # Store the numbers in each column.
        cols = [set() for _ in range(9)]
        # 存放 3x3的小方塊的數字
        # Store the numbers in each 3x3 box.
        boxes = [set() for _ in range(9)]

        # 遍歷整個棋盤
        # Iterate through the entire board.
        #遍歷行
        # Iterate through each rows.
        for r in range(9): 
            #遍歷列
            # Iterate through each columns.
            for c in range(9): 
                #取得當前數字
                # Get the current number.
                num = board[r][c]
                # 如果是空格,直接跳過
                # If the character is a space, skip it.
                if num == '.':
                    continue
                # 知道當前數字是哪個3x3的小方塊
                # Identify the 3x3 subgrid the current number .
                box_index = (r // 3) * 3 + (c//3)

                # 檢查數字是否有出現,有則直接跳出無效
                # Check if the number has already appeared; if so, exist as invalid.
                if (num in rows[r]) or (num in cols[c]) or (num in boxes[box_index]):
                    return False
                
                # 沒出現則加入對應的集合中
                # If it has not appeared, add it to the corresponding sets.
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
            
        return True

        
# @lc code=end

