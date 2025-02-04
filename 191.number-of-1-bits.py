#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        # 循環計算
        while n:
            # 提取n的最低有效位
            # ex. 1011 & 0001 = 0001 (1)
            # count += 1 → 1
            count += n & 1
            # 右移一位,丟掉已處理的最低有效位
            # ex. 1011 >> 1 = 101
            # 這樣就可以每一位都處理到
            n >>= 1
        return count
        
        

        
# @lc code=end

