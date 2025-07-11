#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # #DFS+Recursion
        # # Base case for recursion: if there are no elements, it's a null node.
        # if not preorder or not inorder:
        #     return None
        # #The first element in preorder is always the root of the current subtree.
        # root_val = preorder[0]
        # root = TreeNode(root_val)

        # #Find the root's position in the inorder traversal to split left/right subtrees.
        # mid_idx = inorder.index(root_val)

        # # Recursively build the left and right subtrees.
        # # Slicing creates copies of the lists, which is not memory-efficient.
        # # Because the root in the preorder is index zero, we can start from index 1 to mid index to calculate the tree
        # root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        
        # # The right subtree's preorder traversal starts after all the left subtree nodes.
        # root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        
        # return root

        #DFS+ Recursion + HashMap
        #Pre-Computer a hash map for O(1) lookups of inorder indices

        inorder_map = {val:idx for idx,val in enumerate(inorder)}

        self.preorder_idx = 0

        return self._build_recursive(preorder, inorder_map, 0, len(inorder) - 1)
    
    def _build_recursive(self,preorder: list[int], inorder_map:dict, in_left:int, in_right:int) -> Optional[TreeNode]:
        #Base case:if the inorder pointers cross, the subtree is empty
        if in_left > in_right:
            return None
        
        # The current root's value is the next available in the preorder sequence.
        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1
        root = TreeNode(root_val)

        #Get the root's index from our pre-computed map to partition the inorder array.
        inorder_mid = inorder_map[root_val]

        # Recursively build the left and right subtrees.
        root.left = self._build_recursive(preorder, inorder_map, in_left, inorder_mid - 1)
        root.right = self._build_recursive(preorder, inorder_map, inorder_mid + 1, in_right)
        
        return root

        
# @lc code=end

