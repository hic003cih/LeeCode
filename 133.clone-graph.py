#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
    # DFS(Depth-First Search)

        # 如果節點不存在，則返回None
        # If the node does not exist, return None
        if not node:
            return None
        
        # 創建一個字典，用於存儲已訪問過的節點
        # Create a dictionary to store the visited nodes
        visited = {}

        def dfs(node):

            # 如果節點已經訪問過，則返回已訪問的節點
            # If the node has been visited, return the visited node
            if node in visited:
                return visited[node]
            
            # 如果節點還未訪問過，則複製該節點
            # If the node has not been visited, copy the node
            copy = Node(node.val)
            # 將該節點標記為已訪問
            # Mark the node as visited
            visited[node] = copy

            # 先遍歷該節點的所有鄰居
            # Traverse all the neighbors of the node
            for neighbor in node.neighbors:
                # 遞歸訪問該節點的所有鄰居
                # Recursively visit all the neighbors of the node
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
        
# @lc code=end

