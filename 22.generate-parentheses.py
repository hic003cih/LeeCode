#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# Backtracking -> Recursion and Trial & Error & Pruning
# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []

        # def backtrack(current, open_count, close_count):
            

        #     # 若字串長度達到 2*n，表示生成了一組完整的括號
        #     if len(current) == 2 * n:
        #         result.append(current)
        #         return
            
        #     # 先執行這部分,加入n個(
        #     if open_count < n:
        #         backtrack(current + "(", open_count + 1, close_count)

        #     # 加入n個(後,再加入n個)
        #     if close_count < open_count:
        #         backtrack(current + ")", open_count, close_count + 1)
        # # 回朔 open_count, close_count不會減少
        # # 初始呼叫
        # backtrack("", 0, 0)
        # return result

        res =[]

        def backtrack(left, right, path):
            # 如果左右括號都用完,加入結果
            # If both left and right parentheses are used up, add to the result
            if left == n and right == n:
                res.append("".join(path))
                return
            
            # 可以放'(' (左括號), 但不能超過n個
            # A '(' can be placed, but the count cannot exceed n.
            if left < n:
                # 將新的元素append上
                path.append("(")
                # 進入到下一個節點
                # Recur with one more '(' added
                backtrack(left + 1, right, path)
                # Backtrack (undo the choice)
                path.pop()

            # 可以放')' (右括號), 但不能超過左括號的數量
            # A ')' can be placed, but the count cannot exceed the number of left parentheses.
            if right < left:
                path.append(")")
                # Recur with one more ')' added
                backtrack(left, right + 1, path)
                # Backtrack (undo the choice)
                path.pop()

        # Start the recursion with 0 left and right parentheses used
        backtrack(0, 0, [])
        return res
        
# @lc code=end

