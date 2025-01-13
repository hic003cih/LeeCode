#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):

        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(s):
            current_value = roman_to_int[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total



    # total = 0
    # prev_value = 0

    # for char in reversed(s):
    #     current_value = roman_to_int[char]

    #     if current_value < prev_value:
    #         total -= current_value
    #     else:
    #         total += current_value

    #     prev_value = current_value
        
    # return total

    
        
# @lc code=end

