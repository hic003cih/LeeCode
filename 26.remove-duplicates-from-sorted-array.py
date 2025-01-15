#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        slow = 0 #Pointer to track the last unique element
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]: #Found a unique element
                slow += 1
                nums[slow] = nums[fast] #Update the position for the unique element
        return slow + 1 #The count of unique elements
# @lc code=end

