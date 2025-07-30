#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # 1. Dynamic Programming
        # # A trivial case: if the list is empty, the LIS is 0.
        # if not nums:
        #     return 0
        # n = len(nums)
        # # dp[i] will store the length of the LIS ending at index i.
        # # Initialize every LIS to be at least 1 (the element itself).
        # dp = [1] * n

        # # Iterate through the array starting from the second element.
        # for i in range(1,n):
        #     # Check all previous elements to see if they can extend a subsequence.
        #     for j in range(i):
        #         # If nums[i] can be appended to the LIS ending at nums[j]...
        #         if nums[i] > nums[j]:
        #             # ...update dp[i] if we found a longer subsequence.
        #             dp[i] = max(dp[i], dp[j] + 1)
        # # The length of the LIS is the maximum value in our dp array.
        # return max(dp)

        # 2. Greedy Algorithm with Binary Search
        # `sub` will store the smallest tail of all increasing subsequences.
        # with length i+1 at sub[i]
        sub =[]

        for num in nums:
            # Find the first position in `sub` where `num` can be inserted
            # to maintain the sorted order. This is equivalent to finding the 
            # first element >= num.
             # bisect_left performs a binary search.
            idx = bisect_left(sub, num)
            # If `idx` is equal to the length of `sub`, it means `num` is
            # greater than all elements currently in `sub`.
            if idx == len(sub):
                # Append `num` to extend the longest subsequence found so far.
                sub.append(num)
            else:
                # Replace the element at `idx` with `num`. This helps to
                # potentially form a longer subsequence later with a smaller tail.
                sub[idx] =num
        return len(sub)
                
# @lc code=end

