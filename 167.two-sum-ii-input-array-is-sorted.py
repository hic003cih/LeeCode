#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # #1. Brute-force approach
        # # O(n^2) time complexity, likely to cause a Time Limit Exceeded(TLE) error on large inputs.

        # n = len(numbers)
        # if n <2:
        #     return []
        # for i in range (n-1):
        #     for j in range(i+1,n):
        #         if target == numbers[i] + numbers[j]:
        #             # The problem asks for 1-based indices, so we add 1 to each.
        #             return [i+1,j+1]
        # # Return an empty list if no solution is found
        # return []

        # # 2. Hash Map approach
        # # Time Complexity: O(n)
        # # Space Complexity: O(n)
        # n = len(numbers)
        # if n <2:
        #     return []
        # # The map stores {number:index} pair we have seen so far.
        # seen = {}

        # for i,num in enumerate(numbers):
        #     #Calculate the complement and check if it has been seen before.
        #     complement = target - num
        #     if complement in seen:
        #         # If it exists, we found our pair. Return their 1-based indices.
        #         return [seen[complement]+1,i+1]
        #     #Otherwise, add the current number and its index to the map for future lookups.
        #     seen[numbers[i]] = i
        # return []

        # 3. Two-Pointers approach
        
        n = len(numbers)
        if n <2:
            return []
        
        sorted_num = sorted(numbers)

        left = 0
        right = n-1
        # Search as long as the two pointers have not crossed.
        while left <right:
            current_sum=sorted_num[left]+sorted_num[right]
            if current_sum ==target:
                return [left+1,right+1]
            # The sum is too small, move the left pointer to a larger value.
            elif current_sum < target:
                left +=1
            else: # current_sum > target
                # The sum is too large, move the right pointer to a smaller value.
                right -=1
        return []


        
# @lc code=end

