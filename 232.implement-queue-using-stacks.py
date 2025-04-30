#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):

    # 客製化first in first out的que
    def __init__(self):
        #存第一次進來的stack
        self.in_stack = []
        # 存執行move後倒過來的stack
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 把新進來的數字加進in_stack
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # 先把in_stack的資料倒轉後移到out_stack
        # reverse the order of elements in in_stack and append them to out_stack
        self.move()
        return self.out_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        # 先把in_stack的資料倒轉後移到out_stack
        # reverse the order of elements in in_stack and append them to out_stack
        self.move()
        # 回傳out_stack的最後一個數字
        # return the last element of out_stack
        return self.out_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack
    
    def move(self):
        # 只有 out_stack 是空的時候，才搬 in_stack 的資料過來,避免浪費資源
        # 單靠 stack 自己，無法直接做 queue 的「先進先出」行為！需要倒過來（reverse）
        if not self.out_stack:
            while self.in_stack:
                # 把 in_stack 的資料一個一個pop出來塞入stackout_stack
                self.out_stack.append(self.in_stack.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

