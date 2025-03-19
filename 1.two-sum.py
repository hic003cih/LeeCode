#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
	def twoSum(self, nums, target):
		# seen = {}
		# for i, num in enumerate(nums):
		# 	diff = target - num
		# 	if diff in seen:
		# 		#如果有存在seen中,則直接返回,不用全部都要找一遍
		# 		#seen[diff] ->seen[2] = 0是
		# 		return [seen[diff], i]
		# 	#如果不存在seen中,將num存入,並給index
		# 	seen[num] = i

		# 暴力法
		# 不需要用到額外空間,但比較慢
		# for i in range(len(nums)):
		# 	for j in range(i + 1,len(nums)):
		# 		if nums[i] + nums[j] == target:
		# 			return [i, j]

		# return []

		# 使用 HashMap
		# 需要用到額外空間,但比較快
		num_map ={}
		# enumerate(nums) 讓我們同時獲取索引值 (i) 和對應的元素 (num)
		for i, num in enumerate(nums):
			complement = target - num
			if complement in num_map:
				return [num_map[complement], i]
			# 如果沒找到對應的值,將當前元素存入 HashMap
			# 方便快點找到
			num_map[num] = i

solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))
		
# @lc code=end

