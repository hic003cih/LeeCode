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
        # #Brute-Force approach
        # #This Method  has high complexity and is prone to Time Limit Exceeded(TLE) errors for larger inputs.
        # n = len(height)
        # max_area = 0
        # # Outer loop : 'i' represents the left boundary of a potential container.
        # for i in range(n):
        #     # Inner loop: 'j' represents the right boundary of the container, always to the right of 'i'
        #     for j in range(i+1,n):
        #         # Calculate the width between the current left(i) and right(j) boundaries
        #         width = j-i
        #         #The effective height of the container is limited by the shorter of the two lines (to prevent water from spilling).
        #         h = min(height[i],height[j])
        #         # Calculate the current area formed by these two lines
        #         current_area = h * width
        #         # Update the max_area if the current_area is larger
        #         max_area = max(max_area, current_area)
        
        # return max_area
        
        # Two-Pointer
        # Optimal approach
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        
        # The core idea is to use two pointers and shrink the search space.
        while left < right:
            width = (right-left)
            # The effective height is limited by the shorter of the two lines (to prevent water from spilling).
            h = min(height[left], height[right])
            # Calculate the current area formed by these two lines
            area = width * h
            # Update the max_area if the current_area is larger
            max_area = max(max_area,area)

            # Move the pointer pointing to the shorter line inward.
            # This is because moving the taller line's pointer would not increase the height.
            # And would only decrease the width, thus certainly resulting in a smaller or equal area.
            # Moving the shorter line's pointer might lead to a lager height and thus a potentially lager area.
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area

# @lc code=end

