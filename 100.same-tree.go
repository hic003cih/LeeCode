/*
 * @lc app=leetcode id=100 lang=golang
 *
 * [100] Same Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }

 Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

*/
func isSameTree(p *TreeNode, q *TreeNode) bool {
	//如果都為空,表示一樣,回傳true
	if p == nil && q == nil {
		return true
	}
	//如果其中有一個為空,直接回false,然後值不一樣,回false
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}
	//循環執行節點檢驗,如果都一樣,則繼續執行isSameTree到tree的尾端
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

// @lc code=end

