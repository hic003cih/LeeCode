#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs

#f(5) -> f(4) + f(3)
#   -> (f(3) + f(2)) + (f(2) + f(1))
#   -> ((f(2) + f(1)) + f(2)) + (f(2) + f(1))
#   -> ((2 + 1) + 2) + (2 + 1)
#   -> 8

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Base cases
        if n == 1:
            return 1
        if n==2:
            return 2

        #Two variables to keep track of the two steps
        prev1, prev2 = 1, 2

        #Iteratively calculate the number of ways to climb to step `n`
        #從3開始,因為1,2的結果是固定的
        for _ in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return prev2

# @lc code=end

