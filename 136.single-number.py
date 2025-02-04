#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# a=4 的二進制表示為 100ll

# b=1 的二進制表示為 001
# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            #result = result ^ num
            # result = 0 ^ 4 = 4
            # result = 4 ^ 1 = 5
            # result = 5 ^ 2 = 7
            # result = 7 ^ 1 = 6
            # result = 6 ^ 2 = 4
            result ^= num #XOR all numbers
        return result
# @lc code=end

