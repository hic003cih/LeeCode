/*
 * @lc app=leetcode id=83 lang=golang
 *
 * [83] Remove Duplicates from Sorted List
 */

//  Example 1:

// Input: head = [1,1,2]
// Output: [1,2]
// Example 2:

// Input: head = [1,1,2,3,3]
// Output: [1,2,3]

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {

	//
	//head = [1,1,2]
	current := head
	//
	for current != nil && current.Next != nil {
		//If the current value is the same as the next value, then replace the next value with the value of the node after next
		//Keep check the next value
		if current.Val == current.Next.Val {
			current.Next = current.Next.Next
		} 
		// If the current value is not the same as the next value
		//Move to the next node and continue checking
		else {
			current = current.Next
		}
	}

	return head
}

// @lc code=end

