#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # #移除所有非字母或數字的字符
        # #轉換成小寫
        # s = re.sub(r'[^a-z0-9]', '', s.lower())

        # # s[start:stop:step]
        # # start: 起始索引，從哪裡開始切片（包含）。
        # # stop: 結束索引，在哪裡結束切片（不包含）。
        # # step: 步長，決定每次切片移動的步數（默認為 1）。）
        # #從末尾到開頭逐步取字符，達到字符串反轉的效果
        # #設置為 -1，表示每次切片從右向左移動一個字符，實現字符串反轉。
        # return s == s[::-1]

        #[<expression> for <variable> in <iterable> if <condition>]
        # isalnum 判斷是否為字母或數字
        filtered_chars = ''.join(c.lower() for c in s if c.isalnum())

         # Use two-pointer technique to check palindrome
        left, right = 0, len(filtered_chars)-1
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left +=1
            right -=1
        
        return True
            
        
# @lc code=end

