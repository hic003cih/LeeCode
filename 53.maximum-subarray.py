#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# Dynamic Programming, DP
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = []
        
        # 當前子陣列的總和
        # The sum of the current sub array.
        max_sum = float('-inf')
        # 儲存目前找到的最大子陣列總和
        # Store the maximum sub array sum found so far.
        current_sum = 0


        # for num in nums:
        #     # 是否要重新開始子陣列
        #     # Whether to start a new sub array.
        #     # 當前數字比目前總和加上當前數字還大時，重新開始子陣列。
        #     # If the current number is greater than the sum of the current sum plus current number, start a new sub array.
        #     current_sum = max(num, current_sum + num)
        #     # 更新最大總和,比較最大值和當前的總和
        #     # Update the maximum sum, comparing the maximum sum and the current sum.
        #     max_sum = max(max_sum, current_sum)
        # # 返回最大總和
        # # Return the maximum sum.
        # return 


        # 暴力法（Brute Force）
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum   


        
# @lc code=end

