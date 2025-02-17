#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# Two_pointer Technique
# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = [-1, 0, 1, 2, -1, -4]
        res = []
        # sorted first
        # nums = [-4, -1, -1, 0, 1, 2]
        nums.sort()

        n=len(nums)
        
        # If i = n-1, then left pointer = n, it will go out of range
        #Use for i in range(n - 2) to ensure there are three elements to form three-sum
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointer
            left, right = i + 1 , n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # the total number is too small, so the left pointer moves right to increase total number.
                if total < 0:
                    left +=1
                # the total number is too large, so the right pointer moves left to decrease total number.
                elif total > 0:
                    right -=1
                # if the total number is equal to 0, then append to result list
                # and move the left and right pointer
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1



        
# @lc code=end

