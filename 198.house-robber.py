#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dynamic programming
        # nums = [2, 7, 9, 3, 1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]


        # dynamic programming
        # Space Optimization

        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        
        # prev, prev2 = 0, 0 

        # for num in nums:
        # # nums = [2, 7, 9, 3, 1]
        # # 
        # # prev1->不搶,繼承前一間的值
        # # prev2 + num-> 搶當前的加上前前一間的最大值
        #     new_val = max(prev1, prev2 + num)
        # # 讓 prev2 變成 i-1 的最大金額，這樣下一輪可以正確計算 i-2 的值
        #     prev2 = prev1
        # # 更新 prev1，存儲新的最大值
        #     prev1 = new_val

        # return prev1

# @lc code=end

