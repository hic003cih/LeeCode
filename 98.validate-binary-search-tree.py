#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, lower_bound, upper_bound):
            # 基本情況: 空節點是有效的BST
            # Base case: empty node is a valid BST
            if not node:
                return True
            
            # 檢查節點值是否在有效範圍內
            # Check if node value is within the valid range
            if not (lower_bound < node.val < upper_bound):
                return False
            
            # 遞迴檢查左子樹和右子樹
            # Recursively check left and right subtrees
            return (
                validate(node.left, lower_bound, node.val) and
                validate(node.right, node.val, upper_bound)
            )
    
        # validate(Node(15), 10, float('inf')

        # 初始範圍為無限小和無限大
        # Initial range is negative infinity to positive infinity
        return validate(root, float('-inf'), float('inf'))
            
        
# @lc code=end

