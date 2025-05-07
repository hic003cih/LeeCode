#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 處理邊界情況
        # Handle the edge cases
        if not nums:
            return 0
        
        # 建立數字集合
        # Create a set of numbers
        num_set = set(nums)

        # 初始化最長連續序列的長度
        # Initialize the length of longest consecutive sequence
        longest_streak = 0

        # 遍歷數字集合
        # Iterate over the numbers in the sets
        for num in num_set:
            # 檢查num - 1是否在集合中,如果不在,表示num是地一次出現,是連續序列的起始點
            # Check if num - 1 is in the set, if not, it means num is the first time appearance, it is the starting point of consecutive sequence
            # ex. 先檢查了1,2,3 -> 如果接下來看到2,就跳過,因為2不可能比1,2,3還長,直接跳過節省效率
            # ex> Check 1,2,3 -> If the next one is 2, skip it, because 2 can't be longer than 1,2,3, skip it to save time
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 開始檢查下一個連續數字
                # Start checking the next consecutive number
                while current_num + 1 in num_set:
                    # 如果下一個連續數字存在,更新當前數字和連續序列的長度
                    # If the next consecutive number exists, update the current number and the length of consecutive sequence
                    current_num += 1
                    current_streak += 1

                # 比對連續序列的長度,更新最長連續序列的長度
                # Compare the length of the consecutive sequence, update the length of the longest consecutive sequence
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak



        
        
# @lc code=end

