#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #if either list is empty
        if not headA or not headB:
            return None

        #initialize pointers
        p1, p2 = headA, headB

        # listA = [4, 1, 8, 4, 5]
        # listB = [5, 6, 1, 8, 4, 5]  
        
        #Traverse both lists until they meet or both become null
        while p1!=p2:
            #Switch to the list's head when reaching the end
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        #either they meet at the intersection node, or both are null
        return p1
# @lc code=end

