#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # # Use Method min()
        # return min(nums)

        # # Brute-force / Linear Scan
        # # Handle the edge case of an empty list.
        # if not nums:
        #     return None
        # minimum_value = nums[0]

        # #Iterate through the rest of the list to find the true minimum.
        # for i in range(1,len(nums)):
        #     # If the current number is smaller than our current minimum, update it.
        #     if nums[i] < minimum_value:
        #         minimum_value = nums[i]
        # return minimum_value

        #Binary Search
        #nums = [4, 5, 6, 7, 0, 1, 2]
        # Initialize pointers for the start and end of our search space.
        left, right = 0, len(nums) -1

        # The loop continues as long as our search space has more than one element.
        # It will terminate when `left` and `right` converge on the same index.
        while left < right:
            #Calculate the middle index.
            mid = left + (right - left) //2

            # If the middle element is greater than the rightmost one,
            # it means the pivot point (the minimum value) must be in the right half.
            if nums[mid] > nums[right]:
                #Therefore, we can safely discord the entire left half, including the middle element.
                left = mid +1
            else:
                #If the middle element is not greater than the rightmost one,
                # it means the subarray from mid to right is sorted.
                right = mid
        # When the loop terminates, `left` and `right` will be equal
        return nums[left]

# @lc code=end

