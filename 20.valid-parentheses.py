#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true


# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #建立closing bracket
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            #如果char有在bracket_map中,表示是closing bracket的
            #把stack彈出
            #存入#是怕stack是空時,會error
            #如果是),},] -> 才會進入比對
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            #如果不是closing bracket,把char append到stack中
            else:
                stack.append(char)
        #如果最後stack都是一對,都會pop完,最後為空,會回傳true
        return not stack

        if not stack or stack[-1] != pairs[char]:
            
# @lc code=end

