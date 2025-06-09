#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

       #DP
        # res = [0] * (n+1)
        # for i in range(1, n+1):
        #     res[i] = res[i >>1] + (i&1)

        # return res

        # Brute Force
        def count_ones(x):
            """
            Counts the number of '1' bits in the binary representation of an integer x.
            This is a helper function for the brute force approach.
            """
            count = 0
            while x:
                # Check the Least Significant Bit using bitwise AND with 1.
                # If the LSB is 1, 'x &1' will be '1', and we add it to the count
                # count = count + (x&1)
                count += x &1
                # After processing the LSB, right shift x by 1 to remove the LSB.
                # x = x >> 1
                x >>= 1
            return count
        
        return [count_ones(i) for i in range(n+1)]
        
        
# @lc code=end

