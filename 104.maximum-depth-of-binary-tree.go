/*
 * @lc app=leetcode id=104 lang=golang
 *
 * [104] Maximum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	// Recursively calculate the depth of left and right subtrees
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	// Return 1 + the maximum of the two depths
	return 1 + max(leftDepth, rightDepth)
}

// @lc code=end

