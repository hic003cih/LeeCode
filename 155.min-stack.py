#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack =[]
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 直接append在stack的最後面
        # Append val to the end of stack
        self.stack.append(val)
        # 如果min_stack是空的,或是val小於等於min_stack的最後一個元素,直接加入min_stack
        # If min_stack is null, or val is less than or equal to the last element in min_stack, add it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        # 如果pop的元素等於min_stack的最後一個元素,也pop掉min_stack的最後一個元素
        # If the popped element is equal to the last element in min_stack, also pop it from min_stack
        if val== self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # 返回stack中最上層的元素
        # Return the top element from stack
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # 返回min_stack中最上層的元素
        # Return the top element from min_stack
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

