#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # # Brute-force approach
        # if not head or left==right:
        #     return head
        
        # # Traverse and store
        # temp_arr = []
        # current = head
        # index = 1
        # while current:
        #     if index >= left and index <= right:
        #         temp_arr.append(current.val)
        #     current = current.next
        #     index += 1

        # #Reverse the array
        # temp_arr.reverse()

        # #Traverse again and replace values
        # current = head
        # index = 1
        # arr_idx = 0
        # while current:
        #     if index >= left and index <=right:
        #         current.val = temp_arr[arr_idx]
        #         arr_idx += 1
        #     current = current.next
        #     index +=1
        
        # return head

        # head = [1, 2, 3, 4, 5], left =2,right=4

        
        # One-Pass, Pointer Manipulation
        if not head or left==right:
            return head
        
        #Create a dummy node to simplify edge cases like left=1.
        dummy = ListNode(0,head)

        #Find the node just before the reversal part.
        pre = dummy
        for _ in range(left -1):
            pre =pre.next
        
        # `pre` is now the node before the sublist to be reversed.

        #Start reversing.
        current = pre.next

        #`current` is the head of the reversing part. It will stay as a reference point.
        for _ in range(right -left):
            #The node to be moved.
            next_node = current.next
            # detaching and re-linking
            # `current` links to `next_node`'s next.
            current.next = next_node.next
            # Insert `next_node` after `pre`.
            next_node.next = pre.next
            # Update `pre`'s next.
            pre.next = next_node
        
        return dummy.next

# @lc code=end

