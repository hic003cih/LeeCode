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
        # Loop continues as long as n has any '1' bits
        while n:
            # Extract the Least significant bit of 'n' using bitwise AND with1 
            # 提取n的最低有效位
            # ex. 1011 & 0001 = 0001 (1)
            count += n & 1
            # Right shift 'n' by 1 position. This removes the current LSB and moves the next bit to the LSB position.
            # It's equivalent to integer division by 2.
            # 右移一位,丟掉已處理的最低有效位
            # ex. 1011 >> 1 = 101
            # 這樣就可以每一位都處理到

            n >>= 1
           
        return count

        # Brian Kernighan Algorithm
        # The operation turns off the rightmost '1' bit to '0'
        # Loop continues as long as n is not 0
        # while n:
        #     # In each iteration, the operation n = n & (n-1), turns the rightmost 1 bit to 0
        # 7(111) & 6(110) -> 110 6

        # 110 & 101 -> 100 4

        # 100 & 011 -> 000 0
        #     n = n & (n-1)
        #     # Increment the counter each time a '1' bit is turned off.
        #     count+=1
        
        # return count
        

        
# @lc code=end

