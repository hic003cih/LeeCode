#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        #BST is a binary search tree 
        # It is a binary tree where each node has a value greater than the values in its left subtree and less than the values in its right subtree
        if not nums:
            return None

        #Find the middle index
        mid = len(nums) // 2

        #Create the root node
        root = TreeNode(nums[mid])

        #Recursively build the left and right subtrees
        #Left subtree process the first half of the array, with indices from 0 to mid-1
        root.left = self.sortedArrayToBST(nums[:mid])
        #Right subtree process the left half 0f the array, with indices from mid + 1 to the end
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

# @lc code=end

