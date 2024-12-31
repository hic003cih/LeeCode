/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	// l1 = [1, 2, 4]
	// l2 = [1, 3, 4]

	// 1
	//1,1,2,3,4,4

	// [1, 1, 2, 3, 4, 4]

	// Use var head *ListNode when you plan to initialize it explicitly later.
	// Use dummy := &ListNode{} when you want an immediate valid node to work with, especially for linked list problems. It simplifies the logic and avoids edge cases.

	// dummy := &ListNode{}  // Dummy node as placeholder
	// current := dummy

	// for list1 != nil && list2 != nil {
	// 	//小的先放
	// 	if list1.Val < list2.Val {
	// 		//list1比較小,先放入current
	// 		current.Next = list1
	// 		//存入後,跳下一個node
	// 		list1 = list1.Next
	// 	} else {
	// 		//list2比較小,先放入current
	// 		current.Next = list2
	// 		//存入後,跳下一個node
	// 		list2 = list2.Next
	// 	}
	// 	//把list中放入current Node的設成current
	// 	//下次執行current.Next = list1or list2時,才會是新存入的node的next
	// 	current = current.Next
	// }

	// // Attach remaining nodes
	// if list1 != nil {
	// 	current.Next = list1
	// }
	// if list2 != nil {
	// 	current.Next = list2
	// }

	// // 如果return dummy的話,會變成dummy -> 1 -> 2 -> 3, 但只要後面的1 -> 2 -> 3而已,所以只要return dummy.Next
	// return dummy.Next

	//ListNode用法
	var head *ListNode
	if list1.Val < list2.Val {
		head = list1
		list1 = list1.Next
	} else {
		head = list2
		list2 = list2.Next
	}

	current := head
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			current.Next = list1
			list1 = list1.Next
		} else {
			current.Next = list2
			list2 = list2.Next
		}
		current = current.Next
	}

	if list1 != nil {
		current.Next = list1
	} else {
		current.Next = list2
	}

	return head
}

// @lc code=end

