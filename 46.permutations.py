#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
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

        def backtrack(path, visited):
            if len(path) == n:
                # Make a copy of path and store it in result
                # result.append(path) -> It directly stores the reference to path, so after appending 2 and 3, all elements become [1,2,3]
                # result.append(path[:]) -> Make a copy of path, store it in result, and ensure that result remains unaffected by changes to path
                result.append(path[:])
                return

            # Iterate over each number in nums
            for i in range(n):
                #If it hasn't been used yet, set it to True and append it to path.
                # If it has already been used, skip to the next i.
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    # Proceed to the next level and append to path
                    backtrack(path, visited)

                    # After completing all levels, exit backtracking, perform backtracking by popping the last element from path, and set it to False
                    visited[i] = False
                    path.pop()
        
        backtrack([], [False] * n)
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




