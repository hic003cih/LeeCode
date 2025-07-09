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
import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
    #     #Depth-First Search(DFS)
    #     if not root:
    #         return []
    #     results = []

    #     self._dfs(root,0,results)
    #     return results
    
    # def _dfs(self,node,level,results):
    #     #Base case for the recursion.
    #     if not node:
    #         return
    #     # When we first visit a new level, we need to create a new sublist
    #     # The level index corresponds to the list's size at that moment.
    #     if level == len(results):
    #         results.append([])
        
    #     # Add the current node's value to its corresponding level's list.
    #     results[level].append(node.val)

    #     #Recurse for the left and right children at the next level.
    #     self._dfs(node.left, level+1,results)
    #     self._dfs(node.right, level+1,results)

        # Breadth-First Search 廣度優先搜索 (BFS)，通常會藉助一個佇列 (Queue) 

        # # Handle the edge case of an empty tree.
        # if not root:
        #     return []
        # #Use a deque for an efficient O(1) pop from the left.
        # queue = collections.deque([root])
        # results = []

        # while queue:
        #     #At the beginning of each loop, the queue holds all nodes for the current level.
        #     level_size =len(queue)
        #     current_level = []
        #     #Process all nodes for the current level.
        #     for _ in range(level_size):
        #         #Dequeue the node from the front.
        #         node = queue.popleft()
        #         current_level.append(node.val)

        #         #Enqueue children for the next level.
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     results.append(current_level)
        # return results

# @lc code=end

