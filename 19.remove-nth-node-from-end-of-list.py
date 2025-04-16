#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head

        fast = dummy
        slow = dummy
        
        # 先讓 fast 移動 n+1 步,這樣fast到最尾端,slow + 1 的位置就是要刪除的節點
        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow.next 的前一個節點是我們要刪除的節點
        slow.next = slow.next.next

        return dummy.next
        
# @lc code=end

