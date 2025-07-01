#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # Two Passes approach 
        # non_zero_count = 0

        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[non_zero_count] = nums[i]
        #         non_zero_count +=1
        
        # for i in range(non_zero_count,len(nums)):
        #     nums[i] = 0

        # Two Pointers 
        slow = 0

        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

                slow +=1
    

# @lc code=end

