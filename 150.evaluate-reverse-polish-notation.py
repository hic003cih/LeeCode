#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            # 判斷token是不是運算符號
            # If token is an operator, pop the last two elements from stack, perform the operation, and push the result back to stack
            if token in "+-*/":
                # 取出stack的最後兩個元素, 做運算後, 再把結果放回去
                # Pop the last two elements from stack, perform the operation, and push the result back to stack
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # 注意這裡要先轉成float, 不然會有問題
                    # Note that here we need to convert to float first, otherwise there will be problems
                    stack.append(int(a) / b)
            else:
                stack.append(int(token))
        
        return stack[0]
        
# @lc code=end

