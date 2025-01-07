/*
 * @lc app=leetcode id=101 lang=golang
 *
 * [101] Symmetric Tree
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
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	return isMirror(root.Left, root.Right)
}

func isMirror(t1, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if t1 == nil || t2 == nil || t1.Val != t2.Val {
		return false
	}
	return isMirror(t1.Left, t2.Right) && isMirror(t1.Right, t2.Left)
}

// if root == nil {
//         return true
//     }
//     queue := []*TreeNode{root.Left, root.Right}

//     for len(queue) > 0 {
//         t1 := queue[0]
//         t2 := queue[1]
//         queue = queue[2:]

//         if t1 == nil && t2 == nil {
//             continue
//         }
//         if t1 == nil || t2 == nil || t1.Val != t2.Val {
//             return false
//         }

//         queue = append(queue, t1.Left, t2.Right, t1.Right, t2.Left)
//     }

//     return true
// @lc code=end

