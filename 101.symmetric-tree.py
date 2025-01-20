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
            # if both tree is empty, definitely symmetric return True
            if not t1 and not t2:
                return True
            # if only one tree is empty, definitely not symmetric return False
            if not t1 or not t2:
                return False
            # compare values and recursively check left and right subtrees
            return(
                t1.val == t2.val and 
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        # call nested function
        return isMirror(root.left, root.right)


# @lc code=end

