#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#
# 用DP
# s = "aa"
# p = "a*"
# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # Brute-force 
        def dp(i,j):
        # s = "aa", p = "a*"
            if j == len(p):
                return i == len(s)
            # 確保 s[i] 存在（還沒跑到結尾）, s[i] 和 p[j] 一樣 or p[j] 是通配符 .
            first_match = i <len(s) and (p[j] == s[i] or p[j] == '.')

            # 判斷p[j + 1] == '*' 有星號！
            if j + 1 < len(p) and p[j + 1] == '*':
                # 跳過 這個 x*，當作「0 次」, 用掉一個 x，然後還留在 x* 重複使用
                return (dp(i, j + 2) or (first_match and dp(i + 1, j)))
            else:
                # p[j + 1] != '*' ➜ 沒有星號！
                return first_match and dp(i + 1, j + 1)

        return dp(0,0)



        # m, n = len(s), len(p)
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True

        # # 處理 s 是空字串，但 p 有 a* b* 這種情況
        # for j in range(1, n + 1):
        #     if p[j - 1] == '*':
        #         dp[0][j] = dp[0][j - 2]
        
        # for i in range(1, m + 1):
        #     for j in range(1, n +1):
        #         if p[j - 1] == '.' or p[j -1] == s[i-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         elif p[j - 1] == '*':
        #             dp[i][j] == dp[i][j-2]
        #             if p[j-2] == '.' or p[j-2] == s[i-1]:
        #                 dp[i][j] = dp[i][j] or dp[i-1][j]

        # return dp[m][n]

        
        
# @lc code=end

