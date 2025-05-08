#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Recursive Approach
        # 中序遍歷: 左子樹 -> 根節點 -> 右子樹
        # Inorder Traversal: Left Subtree -> Root Node -> Right Subtree

        # 建立一個空的list來存放節點值
        # Create a list to store the node values
        result =[]

        def inorder(node):
            # 如果root為空,返回
            # If root is empty, return
            if not node:
                return
            # 先遍歷這個點的左子樹
            # Traverse the left subtree of this node first
            inorder(node.left)
            # 處理完左子樹後,先將節點值加入到result中
            # After traversing the left subtree, add the node value to result
            result.append(node.val)
            # 繼續遍歷右子樹
            # Traverse the right subtree
            inorder(node.right)
        # 從根部開始執行
        # Start from the root
        inorder(root)

        return result
        
# @lc code=end

