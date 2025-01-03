/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]
// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	//如果不用placeholder,需要先建立一個head存到current,才能用current.next來存下面的node
	// var head *ListNode
	// var current *ListNode

	// for _, val := range values {
	//     newNode := &ListNode{Val: val}
	//     if head == nil { // Special case: Initialize the first node
	//         head = newNode
	//         current = head
	//     } else { // General case: Attach new node to the current node
	//         current.Next = newNode
	//         current = current.Next
	//     }
	// }
	// return head

	//dummy used as a placeholder
	//The dummy node provides a consistent starting point (dummy.Next) for the list.
	//You don't need to check whether head is nil or manage separate logic for the first node.
	// This initializes a new ListNode with default values:

	// dummy.Val = 0 (default for integers in Go).
	// dummy.Next = nil (default for pointers in Go).

	dummy := &ListNode{}
	current := dummy
	carry := 0

	for l1 != nil || l2 != nil || carry != 0 {
		sum := carry
		if l1 != nil {
			//sum = sum + l1.Val
			sum += l1.Val
			//Move to the next node in l1
			l1 = l1.Next
		}
		if l2 != nil {
			//sum = sum + l2.Val
			sum += l2.Val
			//Move to the next node in l2
			l2 = l2.Next
		}

		//If the sum exceeds 10, a carry is needed. Calculate the quotient after dividing the sum by 10.
		carry = sum / 10
		//The node stored the remainder after dividing the sum by 10
		current.Next = &ListNode{Val: sum % 10}
		//Updates the current pointer to the next node.
		//End of operation logic, move to the next node.
		current = current.Next
	}

	return dummy.Next
}

// @lc code=end

