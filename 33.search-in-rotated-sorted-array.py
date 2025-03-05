#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# Binary Search
# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Input: nums = [4,5,6,7,0,1,2], target = 0
        # Output: 4     

        left,right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 #Calculate the middle index

            if nums[mid] == target:
                return mid #Found the target, return its index
    
            #Determine which part is sorted
            if nums[left] <= nums[mid]: #Left half is sorted
                if nums[left] <= target < nums[mid]: #Target is in the left part
                    right = mid - 1
                else: #Target is in the right half
                    left = mid + 1
            else: #Right half is sorted
                if nums[mid] < target <= nums[right]: #Target is in the right half
                    left = mid + 1
                else: #Target is in the left half
                    right = mid - 1
        return -1 # Target not found
                
            
# @lc code=end

