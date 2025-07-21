#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # # 1. Brute-Force Approach
        # if not head or not head.next:
        #     return
        # # Store all nodes in an array.
        # nodes_arr =[]
        # current = head

        # while current:
        #     nodes_arr.append(current)
        #     current = current.next
        
        # #Re-link nodes using two pointers.
        # left, right = 0,len(nodes_arr) - 1
        # while left < right:
        #     # Link from the left side to the right side.
        #     nodes_arr[left].next = nodes_arr[right]
        #     left +=1
        #     # If left and right meet, the right node is already linked, so we can break.
        #     if left == right:
        #         break
        #     # Link from the right side back to the next node on the left side.
        #     nodes_arr[right].next = nodes_arr[left]
        #     right -=1

        # # Handle the tail to prevent cycles
        # nodes_arr[left].next = None

        # 2. Three-step process
        # Divide and Conquer
        if not head or not head.next or not head.next.next:
            return
        #Step1: Find the middle of the linked list
        #We use the fast and slow pointer technique.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At the end of the loop, `slow` is at the middle node.
        # The head of the second half is `slow.next`

        # nums = [1, 2, 3, 4, 5]

        #Step2: Reverse the second half of the list.
        #First, split the list into two halves.
        second_head = slow.next
        slow.next =None

        prev = None
        while second_head:
            temp = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = temp
        # `prev` is now the new head of the reversed second half.

        # Step3: Merge the two halves.
        # first_half points to the head(1->2->3...)
        # second_half points to the reversed end (5 -> 4...)

        first_half, second_half = head, prev
        while second_half:
            temp1,temp2 = first_half.next, second_half.next

            # Weave the lists together.
            first_half.next = second_half
            second_half.next = temp1

            # Move pointers to the next nodes to be merged.
            first_half, second_half = temp1, temp2


        

        
# @lc code=end

