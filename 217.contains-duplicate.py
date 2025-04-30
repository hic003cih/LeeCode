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
        # 用set來存nums的數字,如果有重複的數字,就回傳True
        # Use a set to store the numbers in nums. if there are duplicate numbers, return True
        seen = set()
        for num in nums:
            # 如果seen中有num,就回傳True
            # If seen has num, return True
            if num in seen:
                return True
            # 如果seen中沒有num,就把num加入seen
            # If num is not in seen, add num to seen
            seen.add(num)
        # 如果seen中沒有重複的數字,就回傳False
        # If there are no duplicate numbers in seen, return False
        return False
        

        
# @lc code=end

