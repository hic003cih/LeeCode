#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
# nums = [1, 2, 3, 4]

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        answer = [1] * n

        # 計算左邊的乘積
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # 計算右邊的乘積
        right =1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

        
# @lc code=end

