#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Using binary search
        # Time complexity: O(log n)
        #Initialize left pointer and right pointer

        left = 0
        right = len(nums) - 1

        # 當右指針沒有小於左指針時,迴圈執行
        # Execute the loop while the right pointer is not less than the left pointer
        while left <= right:
            # 從中間開始往兩邊找,左右指針的中間值除以2就是中間值
            # Find the middle using (left + right) / 2 and expand outward
            mid = (left + right) // 2
            # 如果中間值是target,直接返回中間值
            # Return mid if it matches the target
            if nums[mid] == target:
                return mid
            # 如果中間值小於target,表示在target在mid的右邊範圍,所以left pointer 可以直接移到 mid + 1的位置
            # If mid < target, search in the right half by moving left to mid  + 1
            elif nums[mid] < target:
                left = mid + 1
            # 如果中間值大於target,表示在target在mid的左邊範圍,所以right pointer 可以直接移到 mid - 1的位置
            # If mid  > target, search in the right half by moving right to mid - 1
            elif nums[mid] > target:
                right = mid -1 
        # 因為是以左指針的為基準,如果最後不存在左指針的超過右指針停下來,停下來的位置就是應該插入的位置
        # If the target is not found, left surpass right and indicates the insertion index
        return left

        
# @lc code=end

