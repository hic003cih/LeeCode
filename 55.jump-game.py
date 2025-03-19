#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
# Greedy Algorithm
# nums = [3, 2, 1, 0, 4, 5, 6]
# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 最遠可以到達到的位置
        max_reachable = 0

        for i in range(len(nums)):
            # 如果索引無法到達
            if i > max_reachable:
                return False
            # 更新最大可到達範圍(所以中間的索引都可以到達),不用一定要到最遠
            max_reachable = max(max_reachable, i + nums[i])
            # 如果能到達最後一個索引,返回True
            if max_reachable >= len(nums) - 1:
                return True
        return False
       
    
        
# @lc code=end

