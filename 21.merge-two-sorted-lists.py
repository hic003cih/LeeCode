#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify merging
        # 設置為 -1 是為了明確虛擬節點的用途，表明它只是用來輔助合併過程，而不是鏈表的實際數據。
        # 在某些場景中，鏈表中的數值可能為 0，使用 -1 作為虛擬節點值可以避免混淆。
        dummy = ListNode(-1)
        current = dummy # Pointer to track the end of the merged list

        #Traverse both lists
        while list1 and list2:
            # If the value of list1 is less than list2, add list1 to the end of the merged list
            # and move list1 to the next node
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the current pointer to the next node
            current = current.next
        
        # Append the remaining nodes from the non-empty list
        # If list1 is empty, append the remaining nodes from list2
        current.next = list1 if list1 else list2
        
        return dummy.next
# @lc code=end

