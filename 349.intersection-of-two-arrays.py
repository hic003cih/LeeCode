#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
from collections import defaultdict
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # #Brute-force approach for finding the intersection of two lists.
        # result = []
        # # Outer Loop: Iterates through each element in the first list(num1).
        # for num1 in nums1:
        #     # Inner Loop: Compares the current element from nums1 with each element in the second list (nums2)
        #     for num2 in nums2:
        #         # If a matching element is found (num1==num2)
        #         # And this element is not yet in our result list
        #         # Then add it to the result list
        #         if num1 == num2 and num1 not in result:
        #             result.append(num1)

        # return result

        # # Sorting + Two Pointers

        # if not nums1 or not nums2:
        #     return []
        # # Sort both input lists to enable the tow-pointer approach
        # nums1.sort()
        # nums2.sort()

        # n1 = len(nums1)
        # n2 = len(nums2)

        # # Initialize two pointers, one for each list, to traverse them.
        # ptr1 = 0
        # ptr2 = 0
        # result = []

        # # Iterate through the number list
        # while ptr1 < n1 and ptr2 < n2:
        #     # If the element in nums1 is smaller than the element in nums2
        #     # This means nums1[ptr1] cannot be in the intersection with the current nums[ptr2].
        #     if nums1[ptr1] < nums2[ptr2]:
        #         ptr1+=1
        #     # If the element in nums1 is bigger than the current number in nums2
        #     # This means nums1[ptr1] cannot be in the intersection with the current nums[ptr2].
        #     elif nums1[ptr1] > nums2[ptr2]:
        #         ptr2 +=1
        #     else:
        #         # If the elements are equal, a common element is found.
        #         # Add the number to the result if it's not already he last added element (to handle duplicates)
        #         if not result or result[-1] != nums1[ptr1]:
        #             result.append(nums1[ptr1])
                
        #         ptr1 +=1
        #         ptr2 +=1
        # return result
        
        # # Hash Map(Frequency Counting) Approach
        # if not nums1 or not nums2:
        #     return []
        # counts = defaultdict(int)
        # # First pass : Populate the frequency map(counts) with elements from nums1.
        # for num in nums1:
        #     counts[num]+=1
        
        # result_set = set()

        # for num in nums2:
        #     # If the current number from nums2 exists in the counts map and still has remaining count.
        #     if num in counts and counts[num] > 0:
        #         # Add it to our result set
        #         result_set.add(num)
        # return list(result_set)

        #Optimal approach - Using set Intersection
        # Convert both lists to sets, sets inherently handle uniqueness of elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Perform the intersection operation using the '&' operator (or .intersection() method).
        # The result is a new set containing only elements present in both original sets.
        # it can also become: intersection_set = set1.intersection(set2)
        intersection_set = set1 & set2

        return list(intersection_set) 
        
    
# @lc code=end

