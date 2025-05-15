#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # 初始化一個負無限大
        # initialize a negative infinity
        self.max_overall_sum = float('-inf')

        # 定義遞歸函數
        # define recursive function
        def dfs(node: Optional[TreeNode]) -> int:
            # 如果節點為空,返回0
            # If the node is empty, return 0
            if not node:
                return 0
            
            # 遞歸計算左子樹和右子樹的最大路徑和
            # Recursively calculate the maximum path sum of the left and right subtrees
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # 計算包含當前節點的最大路徑和(自己為最後一個node可以加上左右子樹的最大路徑和)
            # Calculate the maximum path sum that includes the current node
            current_max_path_sum = node.val + left_max + right_max
            self.max_overall_sum = max(self.max_overall_sum, current_max_path_sum)

            # 返回包含當前節點的最大路徑和(左右只能選一邊)給父節點
            # Return the maximum path sum that includes the current node to the parent node
            # 父節點用來計算left_max和right_max
            # The parent node uses it to calculate left_max and right_max
            return node.val + max(left_max, right_max)
        
        # 從根部開始DFS
        # Start DFS from the rootl
        dfs(root)
        return self.max_overall_sum
        
# @lc code=end

