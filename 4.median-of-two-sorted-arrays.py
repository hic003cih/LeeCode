#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
# Binary search

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        # 確保B是最長的長度,在A上面做二分法會比較快
        if len(A) > len(B):
            A, B = B, A

        x, y = len(A), len(B)
        # 二分法的範圍是A的起點到終點
        low, high = 0, x
        #開始二分
        while low <= high:
            # 計算A的中間位置
            i = (low + high) //2
            # 計算總長度的中間位置
            # +1 是為了讓無論奇數或偶數，左邊的元素數量都會 >= 右邊
            j = (x+y+1) // 2 - i
            # A[i-1], 因為i是切割後的中間值,要求左邊的最大值,就是i-1
            # [  1   3   7   9 ] -> i= 1, A[1] = 3
            A_left = float('-inf') if i == 0 else A[i -1]
            # A[i], 因為i是切割後的中間值,要求右邊的最小值,就是i
            # [  1   3   7   9 ] -> i= 2, A[2] = 7
            # 如果切割出來的 i == x(A的總長度), 表示右邊沒有元素,就給一個很大的值inf
            A_right = float('inf') if i == x else A[i]
            B_left = float('-inf') if j == 0 else B[j -1]
            B_right = float('inf') if j == y else B[j]

             # 如果合併後的左半部分的最大值都小於右半部分的最小值
            # 那麼就找到了中位數
            if A_left <= B_right and B_left <= A_right:
                 # 如果兩個數組的總長度是偶數, 中位數是左半部分的最大值和右半部分的最小值的平均值
                 if (x + y) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                 else:
                    # 如果兩個數組的總長度是奇數, 中位數是兩個左半部中的最大值
                     return max(A_left, B_left)
            # 如果分割不合法(左邊比右邊大)，就移動 binary search 的範圍
            # A 左邊太大 → A 切得太「偏右」了,我們應該往左縮小分割點
            elif A_left > B_right:
                high = i - 1
            # A 左邊太小 → 我們應該往右擴大分割點
            # B 左邊最大 > A 右邊最小
            else:
                low = i + 1

            # high = 3, low=0
            #A = [1, 3, 8]
            # B = [2, 4, 5, 6, 7]
        
# @lc code=end

