#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]

        # Generate rows starting from the second row
        for i in range(1, numRows):
            #Star the row with 1
            # 每個首位都一定是1
            row = [1]
            #Fill in the middle values
            #取前一行的數據
            prev_row = result[i-1] 
            # 從1開始到最尾端
            # 當前一行(prev_row)長度只有0和1時,沒有中間元素,不會執行遍歷
            # 大於1時才要填充中間元素(range(1, 2 or 更大))
            for j in range(1, len(prev_row)):
            # row[j]=prev_row[j−1]+prev_row[j]
            # range(1, len(prev_row)) = range(1, 2)
            # j = 1，計算 prev_row[0] + prev_row[1] = 1 + 1 = 2。
            # 將 2 加入 row，形成 [1, 2]。
                row.append(prev_row[j-1] + prev_row[j])
            #End the row with 1
            # 每個尾部都一定是1
            row.append(1)
            # Append the row to the result
            # 將生成的第 j 行添加到 Pascal's Triangle
            result.append(row)
        return result
        
# @lc code=end

