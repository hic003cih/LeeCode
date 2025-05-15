#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 廣度優先搜索 (BFS)，通常會藉助一個佇列 (Queue) 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # 先處裡邊界條件,如果root為空,返回空list
        # handle edge case, if root is empty, return empty list
        if not root:
            return []
        # 初始化結果列表和隊列
        # initialize result first and queue
        result = []
        # 初始化佇列並加入根節點
        # initialize queue and add root node
        queue = [root]

        while queue:
            # 獲得當前層的節點數量
            # get the number of nodes in the current level
            level_size = len(queue)
            # 初始化當前層的節點值列表
            # initialize list to store node values in the current level
            current_level_values = []

            # 處理當前層的所有節點
            # process all nodes in the current level

            for _ in range(level_size):
                # 從隊列中取出節點
                # pop node from queue
                node = queue.pop(0)
                # 將節點值加入當前層列表
                # add node value to current level list
                current_level_values.append(node.val)

                # 如果節點有左子節點,將左子節點加入隊列
                # if node has left child, add left child to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 將當前層的節點值列表加入結果列表
            # add current level list to result list
            result.append(current_level_values)
        
        # 返回結果
        # return result
        return result



        
# @lc code=end

