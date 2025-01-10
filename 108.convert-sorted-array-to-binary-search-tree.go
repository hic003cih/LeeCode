/*
 * @lc app=leetcode id=108 lang=golang
 *
 * [108] Convert Sorted Array to Binary Search Tree
 */

//  nums = [-10, -3, 0, 5, 9]
//  輸出:
//  [0 -3 9 -10 nil 5]

// 高度平衡二叉搜索樹 (BST):

// 二叉搜索樹的性質：左子樹的所有節點值小於根節點，右子樹的所有節點值大於根節點。
// 高度平衡：二叉樹中每個節點的左右子樹高度差不超過 1。

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
	// 定義遞歸函數
	var helper func(left, right int) *TreeNode
	helper = func(left, right int) *TreeNode {
		if left > right {
			return nil
		}

		// 選擇中間元素作為根節點
		mid := left + (right-left)/2
		root := &TreeNode{Val: nums[mid]}

		// 遞歸構建左子樹和右子樹
		root.Left = helper(left, mid-1)
		root.Right = helper(mid+1, right)

		return root
	}

	// 初始調用遞歸函數
	return helper(0, len(nums)-1)
}

// @lc code=end

