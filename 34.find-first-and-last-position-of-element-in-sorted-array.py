#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
#Binary Search
# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_position(is_first):
           left, right = 0, len(nums) - 1
           position = -1

           while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                position = mid
                if is_first:
                    # Continue searching left for first occurrence
                    right = mid - 1
                else:
                    left = mid +1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
           return position



        # def find_position(is_first):
        #     left, right = 0, len(nums) -1
        #     position = -1
            
        #     while left <= right:
        #             mid = (left + right) // 2

        #             if nums[mid] == target:
        #                 position = mid #Possible first/last position
        #                 if is_first:
        #                     right = mid - 1 # Continue searching left for first occurrence
        #                 else:
        #                     left = mid + 1 # Continue searching right for last occurrence
        #             elif nums[mid] < target:
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #     return position

        first = find_position(True) #Find first occurrence
        last = find_position(False) # FInd last occurrence

        return [first, last]
            
        
        
# @lc code=end

