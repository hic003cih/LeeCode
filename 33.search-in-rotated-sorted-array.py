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
        # # Brute-force
        # # Iterate through the list from the first to the last element.
        # # The index `i` will be from 0 to len(nums) -1.
        # for i in range(len(nums)):
        #     # Check if the current element is equal to the target.
        #     if nums[i]==target:
        #         # If a match is found, return the current index immediately.
        #         return i
        # # If the loop completes without finding the target, it means the target is not in the list
        # return -1

        #Binary search
        #Initialize pointers for the start and end of the search space.
        left,right =0,len(nums)-1

        # The loop continues as long as the search space is valid.
        while left <=right:
            #Calculate the middle index to avoid potential overflow.
            mid = (left+right)//2
            # Case 1: The target is found at the middle index.
            if nums[mid]==target:
                return mid
            # Case 2: The left half of the array is sorted.
            # This is determined by comparing the leftmost element with the middle element.
            if nums[left] <=nums[mid]:
                # Check if the target is within the range of the sorted left half.
                if nums[left] <=target < nums[mid]:
                    # If it is, shrink the search space to the left half.
                    right = mid-1
                else:
                    # If not, the target must be in the unsorted right half.
                    left = mid +1
            # Case 3: The left half is not sorted
            else:
                # Check if the target is within the range of the sorted right half.
                if nums[mid] < target <= nums[right]:
                    # If it is, shrink the search space to the right half.
                    left = mid +1
                else:
                    # If not, the target must be in the unsorted left half.
                    right = mid -1
        # If the loop finished, the target was not found in the array.
        return -1

# @lc code=end

