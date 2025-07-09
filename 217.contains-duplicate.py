#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # 用set來存nums的數字,如果有重複的數字,就回傳True
        # # Use a set to store the numbers in nums. if there are duplicate numbers, return True
        # seen = set()
        # for num in nums:
        #     # 如果seen中有num,就回傳True
        #     # If seen has num, return True
        #     if num in seen:
        #         return True
        #     # 如果seen中沒有num,就把num加入seen
        #     # If num is not in seen, add num to seen
        #     seen.add(num)
        # # 如果seen中沒有重複的數字,就回傳False
        # # If there are no duplicate numbers in seen, return False
        # return False

        # #Brute-force approach

        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
    
        #Sorting
        # Sort the array first.
        # nums.sort()
        # #Iterate through the sorted array to check for adjacent duplicates.
        # for i in range(1,len(nums)):
        #     #Compare the current element with the previous one.
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False

        #HashMap
        #Use a hash set to store elements we have seen so far.
        seen = set()
        for num in nums:
            #If the current number is already in the set, we've found a duplicate
            if num in seen:
                return True
            seen.add(num)
        
        return False

        

        
# @lc code=end

