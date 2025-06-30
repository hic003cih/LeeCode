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

        # # Brute-force approach
        # # This method has a high time complexity and is prone to Time Limited Exceeded(TLE) errors for larger inputs.

        # n = len(nums)
        # if n < 3:
        #     return []
        # # Using set to store the result and handle duplicate triplets.
        # res_set = set()

        # # Outer loop: 'i' serves as the first element of a potential triplet.
        # for i in range(n-2):
        #     # Second loop: 'j' serves as the second element, always positioned after 'i'.
        #     for j in range(i+1,n-1):
        #         # Inner loop: 'k' serves as the third element, always positioned after 'j'.
        #         for k in range(j+1,n):
        #             if nums[i] +nums[j] +nums[k] ==0:
        #                 # Sort the triplet to ensure uniqueness when adding to the set
        #                 # tuple can convert the sorted list to new tuple
        #                 triple = tuple(sorted((nums[i],nums[j],nums[k])))
        #                 res_set.add(triple)
        # # Convert the set to a list before returning.
        # return [list(t) for t in res_set]

        # # Optimal approach : Sorting + two pointers

        # n = len(nums)
        # if n < 3:
        #     return []
        
        # nums.sort()
        # result = []

        # for i in range(n-2):
        #     # Skip duplicate elements for `nums[i]`. This is crucial to prevent
        #     # generating duplicate triplets in the `result` and also helps in
        #     # improving efficiency by avoiding redundant computations.
        #     if i > 0 and nums[i]==nums[i-1]:
        #         continue
        #     left = i +1
        #     right = n-1

        #     while left < right:
        #         current_sum = nums[i] + nums[left] + nums[right]
        #         if current_sum == 0:
        #             result.append([nums[i],nums[left],nums[right]])
        #             # Skip duplicate elements for the second number (nums[left]).
        #             while left < right and nums[left] == nums[left+1]:
        #                 # Shrink the window
        #                 left+=1
        #              # Skip duplicate elements for the third number (nums[right]).
        #             while left < right and nums[right] == nums[right-1]:
        #                 # Shrink the window
        #                 right -=1
        #             # Shrink the window
        #             left +=1
        #             right -=1
        #         # If the sum is less than zero, increment the left pointer to increase the sum.
        #         elif current_sum <0:
        #             left +=1
        #         # If the sum is greater than zero,decrement the right pointer to decrease the sum.
        #         else:
        #             right -=1
        # return result
        # return [list(t) for t in res_set

        # #Hash Map Approach
        # n =len(nums)
        # if n<3:
        #     return []
        # # Use set to store unique triplets and handle duplicates.
        # res_set = set()
        
        # # Outer loop : Iterate through nums to fix the first element nums[i] of a potential triplet.
        # for i in range(n-2):
        #     # Initialize a has set for efficient lookups of the third number (similar to the 2Sum problem).
        #     seen = set()

        #     for j in range(i+1,n):
        #         # Calculate the required complement for nums[i] and nums[j] to sum to zero
        #         complement = -nums[i] - nums[j]

        #         # if the complement is found in the seen set
        #         # Sort the triplet and convert it to a tuple before adding to res_set to ensure uniqueness.
        #         if complement in seen:
        #             triplet = tuple(sorted((nums[i],nums[j],complement)))
        #             res_set.add(triplet)
        #          #Add the nums[j] to the seen set for further lookups
        #         seen.add(nums[j])
        # return [list(t) for t in res_set
    
# @lc code=end

