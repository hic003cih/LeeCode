#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#  1 -> 2 -> 3 -> 4
#        ^       |
#        |_______|

# slow: 1 -> 2 -> 3 -> 4 -> 2 -> ...
# fast: 1 -> 3 -> 2 -> 4 -> 3 -> ...

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        #initialize slow and fast pointers, both starting at the head of the linked list
        slow, fast = head, head

        #Iterate as long as fast and fast.next are not None
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next #Slow pointer moves one step at a time
            fast = fast.next.next #Fast pointer moves two steps at a time

        return False
        
# @lc code=end

