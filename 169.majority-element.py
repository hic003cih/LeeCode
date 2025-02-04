#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        #Boyer-Moore Voting Algorithm
        for num in nums:
            # when count is 0, update the candidate
            if count ==0:
                candidate = num
            # if candidate is the same as num, count + 1
            # if the num is not the same as candidate, count - 1
            count +=1 if num == candidate else -1

        return candidate
        
# @lc code=end

