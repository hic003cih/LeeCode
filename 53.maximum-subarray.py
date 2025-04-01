#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# Dynamic Programming, DP
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = []
        
        # 當前子陣列的總和
        # The sum of the current sub array.
        max_sum = float('-inf')
        # 儲存目前找到的最大子陣列總和
        # Store the maximum sub array sum found so far.
        current_sum = 0


        # for num in nums:
        #     # 是否要重新開始子陣列
        #     # Whether to start a new sub array.
        #     # 當前數字比目前總和加上當前數字還大時，重新開始子陣列。
        #     # If the current number is greater than the sum of the current sum plus current number, start a new sub array.
        #     current_sum = max(num, current_sum + num)
        #     # 更新最大總和,比較最大值和當前的總和
        #     # Update the maximum sum, comparing the maximum sum and the current sum.
        #     max_sum = max(max_sum, current_sum)
        # # 返回最大總和
        # # Return the maximum sum.
        # return 


        # 暴力法（Brute Force）
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]
        #         max_sum = max(max_sum, current_sum)

        # return max_sum   

        # 前綴和優化暴力
        # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # prefix = [0, -2, -1, -4, 0, -1, 1, 2, -3, 1]
        # n = len(nums)
        # # 建立一個「前綴和陣列」,創建一個n+1的陣列
        # prefix = [0] * (n + 1)

        # # 建立前綴和陣列
        # for i in range(n):
        #     # prefix第一個為0,所以從i+1開始
        #     # 每兩個SubArray建立一個sum的prefix
        #     prefix[i+1] = prefix[i] + nums[i]
        # # 創建一個無限大的sum
        # max_sum = float('-inf')

        # # 遍歷所有可能的子陣列,找到最大的sum
        # # 固定i,j值不斷往前加,然後計算sum
        # # ex. nums[0..1] -> total = prefix[2] - prefix[0]
        # for i in range(n):
        #     # j = i 開始，到 j = n - 1 為止（包含 i，不包含 n）
        #     for j in range(i, n):
        #         # 計算子陣列的總和
        #         total = prefix[j+1] - prefix[i]
        #         max_sum = max(max_sum, total)

        # return max_sum



        # Kadane’s Algorithm（最推薦）
        # Kadane 的關鍵思路 -> 如果目前的子陣列總和 < 0，就捨棄，重新開始！
        # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        current_sum = nums[0]
        max_sum = nums[0]
        # 只要記錄最大值就好了
        # Only keep track of the maximum value.
        for num in nums[1:]:
            # 如果目前的子陣列總和沒有比較好，就捨棄，重新開始！
            # If the current subarray sum is not better, discard it and start a new one.
            current_sum = max(num, current_sum + num)
            # 紀錄當前最大的值
            # Record the current maximum value.
            max_sum = max(max_sum, current_sum)




        
# @lc code=end

