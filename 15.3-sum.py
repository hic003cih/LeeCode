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

        # # 先排序
        # # Sort the data first.
        # nums.sort()
        # n = len(nums)
        # result = []
        # # 先選定固定一個數, 遍歷數組
        # # Select a fixed number and loop through the array.
        # for i in range(n - 2): 
        #     # 如果值是一樣的, 直接跳過,因為一樣的i值再執行一次結果都一樣
        #     # If the values are the same, skip to avoid redundant calculations.
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
            
        #     # 設定左右指針
        #     # Initialize left and right pointers.
        #     left, right = i + 1, n -1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]

        #         # 如果最後是0表示條件符合,將結果append到result
        #         # If the final value is 0, append the result to `result` .
        #         if total ==0:
        #             result.append([nums[i], nums[left], nums[right]])

        #             # 跳過相同的 left 值, 避免重複組合
        #             # Skip duplicate `left`` values to prevent redundant combinations.
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left +=1
        #             # 跳過相同的 right 值, 避免重複組合
        #             # Skip duplicate `right` values to prevent redundant combinations.
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -=1
                    
        #             # 繼續下一組可能的解
        #             # Proceed to the next possible solution.
        #             left +=1
        #             right -=1
        #         # 如果total小於0, 表示需要更大的值加到total中,所以left pointer 往右移動
        #         # If the total < 0, increase the total by moving the left pointer to the right.
        #         elif total < 0:
        #             left +=1
        #          # 如果total大於0, 表示需要更小的值加到total中,所以right pointer 往左移動
        #          # If the total > 0, decrease the total by moving the right pointer to the left.
        #         else:
        #             right -=1
        # return result

        # # nums = [-1, 0, 1, 2, -1, -4]
        # res = []
        # # Sort the array to use the two-pointer technique
        # # nums = [-4, -1, -1, 0, 1, 2]
        # nums.sort()

        # n=len(nums)
        
        # # If i = n-1, then left pointer = n, it will go out of range
        # #Use for i in range(n - 2) to ensure there are three elements to form three-sum
        # for i in range(n-2):
        #     # If nums[i] > 0, the sum will always be greater than 0, so we can exit the loop
        #     if nums[i] > 0:
        #         break
        #     #Skip duplicate elements to avoid repeated triplets
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     # two pointer
        #     left, right = i + 1 , n-1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]

        #         # the total number is too small, so the left pointer moves right to increase total number.
        #         if total < 0:
        #             left +=1
        #         # the total number is too large, so the right pointer moves left to decrease total number.
        #         elif total > 0:
        #             right -=1
        #         # if the total number is equal to 0, then append to result list
        #         # and move the left and right pointer
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])

        #              # Move left pointer to skip duplicates
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1
        #             # Move right pointer to skip duplicates
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             left +=1
        #             right -=1
        # return res

        # 1. 排序 (Sorting)
        nums.sort()

        results = []
        # 2. 固定一個數 (Fixing One Number)

        for i in range(len(nums) - 2 ):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target_sum = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_sum:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right 

        # 3. 雙指針 (Two Pointers)

        

        
# @lc code=end

