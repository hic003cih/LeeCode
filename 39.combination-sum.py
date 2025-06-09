#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 初始化一個空列表 result，用於儲存所有符合條件的組合。
        # Initialize an empty list result to store all combinations that satisfy the condition.
        result = []

        # 遞迴函數 backtrack 用於生成所有符合條件的組合。
        # The recursive function backtrack is used to generate all combinations that satisfy the condition
        def backtrack(current_combination, remaining_target, start_index):
            # 如果目標值 remaining_target 為 0，表示已經找到一組符合條件的組合。
            # If remaining_target is 0, it means we have found a combination that satisfies the condition.
            if remaining_target == 0:
                # 將當前組合添加到結果列表中。
                # Add the current combination to the result list.
                result.append(list(current_combination))
                return
            # 如果目標值 remaining_target 小於 0,表示和已經超過目標值,則返回。
            # If remaining_target is less than 0, it means we have exceeded the target value, so return.
            if remaining_target < 0:
                return
            # 遞迴步驟 (Recursive Step)：遍歷所有候選數字。
            # Recursive Step: Iterate over all candidate numbers.
            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])
                # 遞迴調用 backtrack 函數,生成下一層的組合。
                # Recursively call backtrack function to generate the next layer of combinations.
                # i (仍然是 i，而不是 i + 1，允許重複選擇當前數字)
                # i is still i, not i + 1, allowing duplicate selection of the current number
                backtrack(current_combination, remaining_target - candidates[i], i)

                # 回溯步驟 (Backtracking Step)：從當前組合中移除最後選擇的數字。
                # Backtracking Step: Remove the last selected number from the current combination.
                current_combination.pop()
        
        # 遞迴調用 backtrack 函數,生成所有符合條件的組合。
        # Recursively call backtrack function to generate all combinations that satisfy the condition.
        backtrack([], target, 0)
        return result



        
# @lc code=end

