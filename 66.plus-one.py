#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        #for i in range(start, stop, step):
        #start：起始值，迴圈從這個值開始（包含）。
        # stop：終止值，迴圈在到達這個值前結束（不包含）。
        # step：步長，控制每次遞增或遞減的量。

        #Traverse the digits from the last one to the first
        for i in range(n-1, -1, -1):
            digits[i] +=1
            if digits[i] < 10:
                return digits # No carry, return result
            digits[i] = 0 # Carry over, set to 0
        # If loop finishes, it means we need an extra digit
        return [1] + digits
# @lc code=end

