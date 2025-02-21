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

        def backtrack(current, open_count, close_count):
            

            # 若字串長度達到 2*n，表示生成了一組完整的括號
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # 先執行這部分,加入n個(
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # 加入n個(後,再加入n個)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        # 回朔 open_count, close_count不會減少
        # 初始呼叫
        backtrack("", 0, 0)
        return result
        
# @lc code=end

