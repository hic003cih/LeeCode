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
        # # Brute-Force Approach
        # if not head or not head.next:
        #     return
        # # Traverse and store nodes
        # nodes_arr =[]
        # current = head

        # while current:
        #     nodes_arr.append(current)
        #     current = current.next
        
        # #Reorder using two pointers
        # left, right = 0,len(nodes_arr) - 1
        # while left < right:
        #     nodes_arr[left].next = nodes_arr[right]
        #     left +=1
        #     # If left and right meet, the right node is already linked, so we can break.
        #     if left == right:
        #         break
        #     nodes_arr[right].next = nodes_arr[left]
        #     right -=1

        # # Handle the tail to prevent cycles
        # nodes_arr[left].next = None

        # Three-step process
        if not head or not head.next or not head.next.next:
            return
        #Find the middle of the linked list
        #We use the fast and slow pointer technique.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #At the end of the loop, `slow` is at the middle node.
        # The head of the second half is `slow.next`

        #Reverse the second half of the list.
        #First, split the list into two halves.
        second_half_head = slow.next
        slow.next =None

        #Standard list reversal logic.
        prev = None
        current = second_half_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        #Merge the two halves.
        #We merge the reversed second half into the first half.
        first_half_head = head
        second_half_head = prev

        #Weave the lists together like a zipper.
        while second_half_head:
            # Temporarily store the next nodes of both lists.
            temp1 = first_half_head.next
            temp2 = second_half_head.next
            # Link first half's node to second half's node.
            first_half_head.next = second_half_head
            #Link second half's node to the original next of the first half.
            second_half_head.next = temp1
            #Move the pointers forward for the next iteration.
            first_half_head = temp1
            second_half_head = temp2

        

        
# @lc code=end

