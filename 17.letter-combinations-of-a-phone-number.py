#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # # Edge case
        if not digits:
            return []

        phone_ ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        # # 23
        # # abc, def
        result = []

        # Depth-First Search (DFS)
        # def dfs(index, path):
        #     # Base case: if the path length equals the digits length
        #     if len(path) == len(digits):
        #         result.append(path)
        #         return
            
        #     for char in phone[digits[index]]:
        #         dfs(index + 1, path + char)
            
        # dfs(0,"")
        # return result

        # 回溯法（Backtracking）

        def backtrack(index, combination):
            if index == len(digits):
                result.append(combination)
                return
            
            letters = phone_map[digits[index]]
            for letter in letters:
                combination.append(letter)
                backtrack(index + 1, combination)
                combination.pop()
        
        # 第一次執行backtrack
        backtrack(0, [])
        return result


    
# @lc code=end

