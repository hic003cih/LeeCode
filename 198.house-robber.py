#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # #1. Brute-force
        # def solve(index):
        #     # Base case: if there are no more houses, we can't rob anything.
        #     if index < 0:
        #         return 0
            
        #     # Option 1: Rob the current house(nums[index]) + max loot from houses before index-1.
        #     rob_this_one = nums[index] + solve(index-2)

        #     # Option 2: Skip the current house and take max loot from houses up to index-1.
        #     skip_this_one = solve(index-1)

        #     return max(rob_this_one, skip_this_one)
        # # Start the process from the last house.
        # return solve(len(nums) -1)

        # # 2. Top-Down DP
        # # memo[i] will store the max money we can rob up to house i.
        # memo = {}
        # def solve(index):
        #     if index < 0:
        #         return 0
        #     # If we have already solved for this index, return the stored value.
        #     if index in memo:
        #         return memo[index]
            
        #     #Rob current house + max loot from two houses down.
        #     rob_this_one = nums[index] + solve(index-2)
        #     # Skip current house, take max loot from the previous house.
        #     skip_this_one = solve(index - 1)
            
        #     # Store the result before returning.
        #     memo[index] = max(rob_this_one, skip_this_one)
        #     return memo[index]
        
        # return solve(len(nums) - 1)

        # # 3. Bottom-Up DP
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n ==1:
        #     return nums[0]
        
        # # dp[i] stores the maximum amount of money that can be robbed up to house i.
        # dp = [0] * n

        # # Base cases
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # # Iterate from the third house to the end.
        # for i in range(2, n):
        #     # The max profit at house i is either:
        #     # 1. Not robbing house i (so profit is the same as at i-1)
        #     # 2. Robbing house i (profit is nums[i] + profit from i-2)
        #     dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # return dp[n-1]

        # 4. Space-optimized DP
        # rob1: max money from robbing up to house i-2
        # rob2: max money from robbing up to house i-1
        rob1, rob2 = 0, 0

        # Iterate through each house.
        # [rob1, rob2, n, n+1, ...]
        for num in nums:
            # For the current house `num`, the new max is either:
            # 1. rob2 (we don't rob the current house `num`)
            # 2. rob1 + num (we rob the current house, so we can't rob the previous one)
            temp = max(rob1 + num, rob2)
            
            # Update the pointers for the next iteration.
            rob1 = rob2
            rob2 = temp
            
        return rob2


# @lc code=end

