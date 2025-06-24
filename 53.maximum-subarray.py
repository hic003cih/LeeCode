#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# Dynamic Programming, DP
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       # # Brute-force approach
        # # This approach has a high time complexity and may exceed time limits
        # n = len(nums)
        # if n ==0:
        #     return 0 
        # #Initialize max_overall_sum with the first element's value
        # max_overall_sum = nums[0]

        # # Outer loop, 'i' represents the staring index of a potential subarray
        # for i in range(n):
        #     current_sum = 0
        #     # Inner loop, 'j' represents the ending index of the current subarray, extending from 'i'
        #     # compare current_sum with max_overall_sum and update if a new maximum is found.
        #     for j in range(i, n):
        #      # Calculate the sum of all subarrays
        #         current_sum = current_sum + nums[j]
        #         max_overall_sum = max(max_overall_sum, current_sum)
        
        # return max_overall_sum
                
       
        # # Dynamic Programming

        # n = len(nums)
        # if n ==0:
        #     return 0 
        
        # #Initialize a DP array of size n 
        # # Base case: The maximum subarray sum ending at index 0 is simply nums[0] itself.
        # dp = [0] * n
        # #Initialize nums[0] as a first element
        # dp[0] = nums[0]

        # # Initialize dp[0] as max_overall_sum
        # max_overall_sum = dp[0]


        # for i in range(1,n):
        #     # This represents the choice between: starring a new subarray at nums[i], or extending the subarray ending at (i-1).
        #     # If nums[i] alone is greater, it signifies that extending the previous subarray would lead to a smaller sum.
        #     dp[i] = max(nums[i],dp[i-1] + nums[i])

        #     # Update the overall maximum sum found so far, as the maximum subarray could end at any point up to 'i'
        #     max_overall_sum = max(max_overall_sum,dp[i])
        
        # return max_overall_sum

        # # Kadane's Algorithm

        # n= len(nums)
        # if n==0:
        #     return 0
        
        # max_sum = nums[0]
        # current_sum = nums[0]

        # for i in range(1,n):
        #     current_sum = max(nums[i],current_sum+nums[i])
        #     max_sum = max(current_sum, max_sum)

        # return max_sum
        

        
# @lc code=end

