#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # # Depth-First Search (DFS)
        # result =[]
        # self._dfs(root,0,result)
        # return result

        #Breath-First Search(BFS)
        if not root:
            return []
        # Use a deque for an efficient queue implementation.
        queue = collections.deque([root])
        result = []

        while queue:
            # At the start of the loop, get the number of nodes on the current level.
            level_size = len(queue)

            # Process all nodes on the current level.
            for i in range(level_size):
                node = queue.popleft()

                # If this is the last node of the current level, add it to the result.
                #This is because we process from left to right.
                if i==level_size -1:
                    result.append(node.val)
                
                # Add children to the queue for the next level's processing.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    # def _dfs(self,node:Optional[TreeNode],depth:int,result:list[int]):
    #     # If the node is null, we've reached the end of a branch.
    #     if not node:
    #         return
    #     # The core logic : if the current depth equals the size of our result list,
    #     # it means we are visiting this depth for the very first time.
    #     if depth == len(result):
    #         result.append(node.val)
    #     #We traverse the right subtree first. This ensures that the first time.
    #     #We encounter a new depth, we are guaranteed to be at its rightmost node.
    #     self._dfs(node.right,depth+1,result)
    #     self._dfs(node.left,depth+1,result)

# @lc code=end

