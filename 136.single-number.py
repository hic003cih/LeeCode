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
            result ^= num #XOR all numbers
        return result
# @lc code=end

