#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0) # dummy node to simplify code
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:l1 = l1.next
            if l2:l2 = l2.next


        return dummy_head.next


        # dummy_head = ListNode(0) # dummy node to simplify code
        # current = dummy_head
        # carry = 0 # Carry for sum > 9
      
        # # l1 = [2, 4, 3] (代表 342) , l2 = [5, 6, 4] (代表 465)
        # # 從後面到前面
        # # [7, 0, 8]  (代表 807)
        # while l1 or l2 or carry:
        #     val1 = l1.val if l1 else 0
        #     val2 = l2.val if l2 else 0

        #     # Compute sum and carry
        #     total = val1 + val2 + carry
        #     # 10 // 10 = 1  (進位)
        #     carry = total // 10 # Compute new carry
        #     # 建立 ListNode(0) -> total % 10 => 10 % 10 -> 0
        #     current.next = ListNode(total % 10) # Store the last digit

        #     #Move forward
        #     current = current.next
        #     # 如果 l1 還有下一個節點，則 l1 = l1.next，繼續遍歷
        #     # 確保 l1 不是 None
        #     if l1: l1 = l1.next
        #     if l2: l2 = l2.next

        # return dummy_head.next # Return the actual result 

# @lc code=end

