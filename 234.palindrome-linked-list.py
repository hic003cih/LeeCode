#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        if not head or not head.next:
            return True

        slow = head
        fast = head

        #  fast 還沒到底，就繼續走。
        # If fast pointer is not yet end, keep going
        while fast and fast.next:
            # slow pointer 移動一步
            # slow pointer moves one step
            slow = slow.next
            # fast pointer 移動兩步
            # fast pointer moves two steps
            fast = fast.next.next

        # fast到底以後, slow會剛好到中間
        # When fast pointer reaches the end, slow pointer is at the middle
        # prev用來存後半段的開頭
        # prev is used to store the beginning of the second half
        # The last node points to None
        prev = None
        # 開始反轉
        # Start reversing
        while slow:
            # 先保存slow的下一個節點
            # Save the next node of slow
            next_node = slow.next
            # 把slow的下一個節點指回前一個節點
            # Point the next node of slow to the previous node
            # 反轉的動作
            # Reverse the action
            slow.next = prev
            # 更新prev為目前的slow位置
            # Update prev to the current position of slow
            prev = slow
            # 更新slow的位置為下一個node
            # Update slow
            slow = next_node
        

        # 比較前半段和反轉後的後半段
        # 指向鏈表最開頭（原本的head）
        # Compare the first half and the reversed second half
        left = head
        # 指向反轉後半段的開頭（prev 是反轉後的新頭）
        # Point to the beginning of the reversed second half (prev is the new head of the reversed second half)
        right = prev

        # 只需要走反轉後半段的長度
        # Only need to through half part 
        while right:
            # 如果值不同則直接跳出
            # If the left value and right value are different,  jump out the loop
            if left.val != right.val:
                return False
            left = left.next
            right = right.next


        
# @lc code=end

