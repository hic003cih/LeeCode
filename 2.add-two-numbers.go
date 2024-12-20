package leetcode

/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// Initialize a dummy node to simplify the code
	dummy := &ListNode{}
	current := dummy
	carry := 0

	// Traverse both lists
	for l1 != nil || l2 != nil {
		// Get the values from the current nodes, if they exist
		var x, y int
		if l1 != nil {
			x = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			y = l2.Val
			l2 = l2.Next
		}

		// Calculate the sum and the carry
		sum := x + y + carry
		carry = sum / 10
		current.Next = &ListNode{Val: sum % 10}
		current = current.Next
	}

	// If there's a remaining carry, add a new node
	if carry > 0 {
		current.Next = &ListNode{Val: carry}
	}

	// Return the next node of dummy, which is the head of the new list
	return dummy.Next
}
