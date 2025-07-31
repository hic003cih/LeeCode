#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 1. Brute-Force
        # def solve(rem):
        #     if rem==0:
        #         return 0
        #     # Base case: if remaining amount is negative, this path is invalid.
        #     if rem < 0:
        #         return float('inf')
            
        #     # Initialize min_coins to infinity for this subproblem.
        #     min_coins = float('inf')

        #     # Try every possible coin.
        #     for coin in coins:
        #         result = solve(rem-coin)
        #         # If a valid solution was found for the subproblem..
        #         if result != float('inf'):
        #             # ...update our minimum.
        #             min_coins = min(min_coins, result + 1)
        #     return min_coins
        
        # ans = solve(amount)
        # return ans if ans != float('inf') else -1

        # # 2. Top-down DP
        # # Memoization cache to store results for each amount.
        # memo = {}

        # def solve(rem):
        #     if rem ==0: return 0
        #     if rem < 0: return -1

        #     # If the result for this amount is already cached, return it.
        #     if rem in memo:
        #         return memo[rem]
        #     min_count = float('inf')

        #     for coin in coins:
        #         res = solve(rem -coin)
        #         if res !=-1:
        #             min_count = min(min_count, res +1)
        #     # Store the result in the cache before returning
        #     memo[rem] = min_count if min_count != float('inf') else -1
        #     return memo[rem]
        # return solve(amount)

        # 3. Bottom-Up DP
        dp = [float('inf')] * (amount +1)

        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >=0:
                    dp[i] = min(dp[i], 1+dp[i -coin])
        return dp[amount] if dp[amount] != float('inf') else -1


# @lc code=end

