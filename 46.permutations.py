#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations 
# backtracking
# nums = [1,2,3]
# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        n = len(nums)

        # def backtrack(path, visited):
        #     if len(path) == n:
        #         # Make a copy of path and store it in result
        #         # result.append(path) -> It directly stores the reference to path, so after appending 2 and 3, all elements become [1,2,3]
        #         # result.append(path[:]) -> Make a copy of path, store it in result, and ensure that result remains unaffected by changes to path
        #         result.append(path[:])
        #         return

        #     # Iterate over each number in nums
        #     for i in range(n):
        #         #If it hasn't been used yet, set it to True and append it to path.
        #         # If it has already been used, skip to the next i.
        #         if not visited[i]:
        #             visited[i] = True
        #             path.append(nums[i])
        #             # Proceed to the next level and append to path
        #             backtrack(path, visited)

        #             # After completing all levels, exit backtracking, perform backtracking by popping the last element from path, and set it to False
        #             visited[i] = False
        #             path.pop()
        
        # backtrack([], [False] * n)
        # return result

        path =[]

        def backtrack(used):
            if len(path) == len(nums):
                # 複製當前的path到result中返回結果
                # Copy the current path to result and return
                # 如果是直接append result,因為是reference,所以後面result再變動的話,結果也會跟著變動
                # If you append directly, it stores a reference - later changes will affect results
                result.append(path[:])
                return
            for i in range(len(nums)):
                # 如果已經出現過,就跳過
                # If it is already appeared, skip it 
                if used[i]:
                    continue
                # 將出現過的數字標記
                # Mark this number as used
                used[i] = True
                # 將數字加入path
                # Put the number into the path
                path.append(nums[i])
                # 遞迴呼叫進入下一層
                # Recursively call to the next level
                backtrack(used)
                # 回溯,把數字退出
                # Backtrack, remove the number
                path.pop()
                # 將退出的數字標記為未使用
                # Mark the number as unused during backtracking
                used[i] = False
        
        # 建立一個與 nums 長度相同的 used 陣列，初始值為 False
        # Create a boolean array 'used' the same length as nums, all set to False 
        used = [False] * len(nums)
        # 開始第一次進入回溯演算法
        # Start the first call of the backtracking algorithm
        backtrack(used)
        # 回傳排列結果
        # Return all generated permutations
        return result

        # result = []
        # n = len(nums)

        # def backtrack(path, visited):
        #     if len(path) == n: # Base case: when the current permutation is complete
        #         result.append(path[:]) # Store a copy of the current permutation -> 怎麼用?
        #         return

        #     for i in range(n):
        #         if not visited[i]: #If the number is not used in the current path
        #             visited[i] =True #Mark the number as used
        #             path.append(nums[i]) #Add the number to the current path

        #             backtrack(path, visited) #Recursively generate the remaining permutations

        #             # Backtrack: remove the last added number and mark it as unused
        #             path.pop()
        #             visited[i] = False

        # backtrack([], [False] * n) # Start the recursion with an empty path and unused numbers
        # return result

# @lc code=end




