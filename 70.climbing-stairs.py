#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # # 1. Brute-force + Fibonacci sequence
        # # Base cases:
        # if n ==1:
        #     return 1
        # # For steps2, there are 2 ways.(1+1 or 2).
        # if n==2:
        #     return 2
        
        # # Recursive step based on the Fibonacci relationship.
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # # 2. Top-Down DP
        # # Memoization cache to store results of subproblems.
        # memo ={}

        # def climb(current_n):
        #     # If the result is already computed, return it.
        #     if current_n in memo:
        #         return memo[current_n]
            
        #     # Base cases.
        #     if current_n <=2:
        #         return current_n
        #     #Compute the result, store it, and then return it.
        #     result = climb(current_n -1) + climb(current_n -2)
        #     memo[current_n] = result
        #     return result
        
        # return climb(n)

        # # 3. Bottom-Up DP
        # if n <= 2:
        #     return n
        
        # # dp[i] will store the number of ways to climb to the i-th step.
        # # We need size n+1 because we want to access dp[n].
        # dp = [0] * (n+1)

        # # Base cases
        # dp[1] = 1
        # dp[2] = 2

        # #Fill the DP table using the recurrence relation.
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        # 4. Space-Optimized Dynamic Programming
        # Base cases for n=1 and n=2
        if n <=2:
            return n
        
        # `a` represents the number of ways to reach step (i-2)
        # `b` represents the number of ways to reach step (i-1)
        a, b = 1, 2

        # Iterate from the 3rd step up to the n-th step
        for _ in range(3, n+1):
            # The number of ways to reach the current step is the sum of the previous two.
            current_ways = a+b
            # Update the pointers for the next iteration.
            a = b
            b = current_ways
        return current_ways
        
# @lc code=end

