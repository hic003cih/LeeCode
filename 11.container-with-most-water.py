#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

    # width = right - left
    # height = min(height[left], height[right])

        left, right = 0, len(height) - 1
        max_area = 0

        #右指針比左指針大,表示還在找最大值
        while left< right:
            # 找出左右兩邊的最大值
            width = (right - left)
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # 移動較矮的指針才能得到最大的
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
                
        return max_area
        
# @lc code=end

