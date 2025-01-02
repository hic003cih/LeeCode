/*
 * @lc app=leetcode id=94 lang=golang
 *
 * [94] Binary Tree Inorder Traversal
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

// Example 1:

// Input: root = [1,null,2,3]

// Output: [1,3,2]

// Example 2:

// Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

//   1
// 2 3
//4 5 null 8
//null null 6 7 9
// Output: [4,2,6,5,7,1,3,9,8]

func inorderTraversal(root *TreeNode) []int {
	var result []int
	var traverse func(node *TreeNode)

	//Recursive function for traversal
	traverse = func(node *TreeNode) {
		//檢查該node有沒有值,沒有值就跳出,繼續做其他的traverse
		//如果是看Left,沒有值則append節點去result
		if node == nil {
			return
		}
		// Traverse the left subtree
		traverse(node.Left)
		// Visit the root node
		result = append(result, node.Val)
		// Traverse the right subtree
		traverse(node.Right)
	}

	//執行tree的遍歷
	traverse(root)
	return result
}

// @lc code=end

