#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# target = 7
# nums = [2,3,1,2,4,3]
# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        # 初始化一個無限大的值
        min_len = float('inf')

        # 右指針向右移動
        for right in range(len(nums)):
            # total直接加上
            total += nums[right]
            # 如果total大於等於target,就減掉左指針的值,左指針向右移動
            # 如果還是超過則繼續縮小找到最小的長度
            while total >= target:
                # 先比對現在的長度,再繼續縮小看看能不能找到最短的長度
                min_len = min(min_len, right - left +1)
                # total超過,所以要減掉左指針的值
                total -= nums[left]
                # 左指針向右移動
                left +=1
        # 如果有值就回傳,沒有就回傳0
        return min_len if min_len != float('inf') else 0
        
# @lc code=end

