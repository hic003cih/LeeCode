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
		# 		# If it exists in seen, return seen[diff] and i directly, avoid unnecessary search
		# 		#seen[diff] ->seen[2] = 0是
		# 		return [seen[diff], i]
		# 	#如果不存在seen中,將num存入,並給index
		#  #If it does not exist in seen, store num and give index
		# 	seen[num] = i

		# 暴力法
		# Brute-force approach
		# 不需要用到額外空間,但比較慢
		# for i in range(len(nums)):
		# 	for j in range(i + 1,len(nums)):
		# 		if nums[i] + nums[j] == target:
		# 			return [i, j]

		# return []

# nums = [2, 7, 11, 15]
# target = 9
	
		# # 初始化一個空的字典,用來存放數字和其索引的對應關係
		# # Initialize an empty dict, used to store num and its index
		# hash_map = {}
		
		# for i, num in enumerate(nums):
		# 	complement = target - num

		# 	# 如果補數(complement)存在於字典中,則返回其索引和當前索引
		# 	# If the complement exists in the dictionary, return its index and the current index
		# 	if complement in hash_map:
		# 		# 返回 'complement' 在雜湊表中的索引 (hash_map[complement])
		# 		# 和當前數字的索引 (i)。
		# 		return [hash_map[complement], i]
			
		# 	# 3.2. 如果 'complement' 不在雜湊表中，
		# 	# If 'complement' is not in the hash map,
		# 	#      我們將當前數字 'num' 及其索引 'i' 存入雜湊表。
		# 	# store the current number 'num' and its index 'i' into the hash map
		# 	#      這樣，如果後續遍歷到另一個數字，它的 'complement' 剛好是 'num'，
		# 	#      the 'complement' of the other number is 'num' if we traverse it later,
		# 	#      我們就可以找到它了。
		# 	#      We can find it later.
		# 	hash_map[num] = i

		# return []

		# # Brute-force approach
		
		# # Iterate through each number, considering it as the first element of a potential pair.
		# for i in range(len(nums)):
		# 	# For each nums[i], iterate through the remaining numbers to its right
		# 	for j in range(i+1,len(nums)):
		# 		# If the sum of the two current numbers equals target, then return the indices of the two numbers
		# 		if target == nums[i] + nums[j]:
		# 			return [i,j]
			
		# return []

		#Hash_Map

		hash_map = {}
		#Iterate through the list numbers
		for i in range(len(nums)):
				# if the complement exists in our hash map. 
				complement = target - nums[i]
				if complement in hash_map:
					# Return the index of the complement and current index 'i'
					return [i, hash_map[complement]]
				# This prepares the map for future numbers to find 'nums' as their complement.
				hash_map[nums[i]] = i 

		return []
				

		


# solution = Solution()

# nums = [2,7,11,15]
# target = 9
# print(solution.twoSum(nums, target))
# @lc code=end
