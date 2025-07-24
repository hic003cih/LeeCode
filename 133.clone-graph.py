#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # # 1. DFS + HashMap
        # # A map to store the mapping from original nodes to their clones.
        # # This prevents infinite loops in case of cycles.
        # cloned_nodes ={}
        # def dfs_clone(original_node):
        #     #If the node is already cloned, return the clone from the map.
        #     if original_node in cloned_nodes:
        #         return cloned_nodes[original_node]
        #     #Create a new node with the same value.
        #     copy_node = Node(original_node.val)

        #     #Add the new node to the map Before traversing its neighbors.
        #     #This handles cycles.
        #     cloned_nodes[original_node] = copy_node

        #     #Recursively clone all the neighbors.
        #     if original_node.neighbors:
        #         for neighbor in original_node.neighbors:
        #             copy_node.neighbors.append(dfs_clone(neighbor))
        #     return copy_node
        # # The entry point of the cloning process.
        # # Handle the case where the input graph is empty.
        # return dfs_clone(node) if node else None

        # 2. BFS + HashMap
        if not node:
            return None
        # Map to store the mapping from original nodes to their clones.
        cloned_nodes = {node: Node(node.val)}

        # Queue for BFS, storing original nodes that need to be processed.
        queue = deque([node])

        while queue:
            # Get the next original node from the queue.
            original_node = queue.popleft()

            # Iterate through all its neighbors.
            for neighbor in original_node.neighbors:
                # If a neighbor has not been cloned yet...
                if neighbor not in cloned_nodes:
                    # Clone it and add it to the map.
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    # and add the original neighbor to the queue to be processed later.
                    queue.append(neighbor)
                # Add the cloned neighbor to the neighbors list of the cloned current node.
                cloned_nodes[original_node].neighbors.append(cloned_nodes[neighbor])
        # Return the clone of the starting node.
        return cloned_nodes[node]

# @lc code=end

