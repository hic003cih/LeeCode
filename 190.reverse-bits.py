#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        
        # range(stop)
        for i in range(32):
            # 提取n的最右位
            # n=13（1101）， n & 1 = 1
            bit = n & 1
            # 將 result 全部左移一位
            # result = 5（0101） -> result << 1 = 10（1010）
            # 將提取的bit位元加到 result 的最低有效位
            # result = 1010，bit =1 -> result=1010∣0001=1011
            result = (result<<1) | bit
            # 右移一位，丟掉已處理的最低有效位，準備提取下一個位元
            # n=13（1101），右移一位後：n=6（‘0110‘）
            n >>= 1
        return result
        
# @lc code=end

