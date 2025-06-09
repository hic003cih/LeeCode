#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 用於儲存所有子集的列表
        # used to store all subsets
        result = []

        def backtrack(subset, index):

            # 將當前子集添加到結果列表中。這是每個遞迴調用都要做的事情，
            # 因為每個 subset 都代表一個有效的子集。
            # 用list 是因為後續的append會修改到subset,所以要用list創建一個新的列表,避免後續的修改影響到result
            # Add the current subset to the result list. This is done for each recursive call, as each subset represents a valid subset.
            # Using list is because subset will be modified later, so we need to create a new list to avoid affecting result
            result.append(list(subset))

            # 遍歷從 index 開始的 nums 陣列中的元素
            # Iterate through the nums array starting from the index
            for i in range(index, len(nums)):
                # 選擇當前元素：將 nums[i] 添加到 subset 中
                # Select the current element: add nums[i] to the subset
                subset.append(nums[i])

                # 遞迴調用 backtrack，從下一個索引 i + 1 開始探索 
                # 這樣可以避免重複（因為每個元素只會被考慮一次）
                # Recursively call backtrack, starting from the next index i + 1
                # This avoids duplicates (because each elements will only be considered once)
                backtrack(subset, i + 1)

                # 回溯：移除 subset 中最後添加的元素
                # 這是為了探索不包含 nums[i] 的其他路徑
                # Backtrack: remove the last added element from the subset
                # This is to explore other paths without nums[i]
                subset.pop()

        # 從空子集和索引0開始調用回溯函數
        # start backtracking from an empty subset and index 0
        backtrack([], 0)
        return result
                

        
        
# @lc code=end

