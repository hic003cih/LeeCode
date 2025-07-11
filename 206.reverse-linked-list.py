#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # #Iteration
        # #'prev' will store the previous node, initialized to None as the nex tail
        # prev = None
        # # 'curr' is the current node we are processing.
        # curr = head

        # while curr:
        #     #Temporarily store the next node before we overwrite curr.next.
        #     #This is a crucial step to not lose the rest of the list.
        #     next_temp = curr.next

        #     #Reverse the pointer of the current node.
        #     curr.next = prev

        #     #Move pointers one position ahead for the next iteration.
        #     prev = curr
        #     curr = next_temp
        # # When the loop ends, 'prev' will be the new head of the reversed list.
        # return prev

        #Recursion
        #Base case for recursion: An empty list or a single-node list is already reversed.
        if not head or not head.next:
            return head

        #Recursively reverse the rest of the list. 'new_head' will be the 
        # head of the reversed sub-list(which is the original list's tail)
        new_head = self.reverseList(head.next)

        #After the sub-list is reversed, head.next is now the tail of that sub-list.
        # We want this node to point back to the current head.
        head.next.next = head

        # The current head becomes the new tail of the entire list, so its next must be None.
        head.next = None

        return new_head




        
# @lc code=end

