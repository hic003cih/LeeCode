#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# 將 isMirror 放在 isSymmetric 中是一種設計模式，稱為內嵌函數（Nested Functions）。這種設計提供了更好的代碼組織方式，使邏輯更加清晰、局部化，並避免命名衝突，是處理輔助邏輯的一種常見做法。
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        #Nested function
        # compare left and right subtrees
        def isMirror(t1, t2):
            # 如果兩個樹都是空,絕對是對稱的
            # if both tree is empty, definitely symmetric return True
            if not t1 and not t2:
                return True
            # 如果一個樹為空,一個不為空,絕對不是對稱
            # if only one tree is empty, definitely not symmetric return False
            if not t1 or not t2:
                return False
            # 如果節點值不等
            # if node value is not equal
            if t1.val != t2.val:
                return False
            # 遞迴比較左右子樹,並且回傳比較後的boolean值
            # compare values and recursively check left and right subtrees, and return boolean value
            return(
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        # call nested function
        return isMirror(root.left, root.right)


# @lc code=end

