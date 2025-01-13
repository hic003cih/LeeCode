#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
	def twoSum(self, nums, target):
		seen = {}
		for i, num in enumerate(nums):
			diff = target - num
			if diff in seen:
				#如果有存在seen中,則直接返回,不用全部都要找一遍
				#seen[diff] ->seen[2] = 0是
				return [seen[diff], i]
			#如果不存在seen中,將num存入,並給index
			seen[num] = i
solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))
		
# @lc code=end

