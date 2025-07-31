#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
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

        # 2. Top-down DP
        



# @lc code=end

