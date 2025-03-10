#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# babad

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = "babad"

        if not s:
            return ""

        # 使用 self 變數來存儲
        # Use the self variable to store data
        self.start, self.max_length = 0, 1  


         # Function to expand around the center
        def expand_around_center(left, right):
            # 提醒系統這是一個 nonlocal 變數,在這個function中才可以使用
            # Declare the variables as nonlocal to indicate that it belongs to an enclosing function's scope, making it accessible only within nested functions.
             #nonlocal start, max_length
             # 從中間開始,左右指針往外擴展
             # Start from the center and expand out word using left and right pointers.
             while left >= 0 and right < len(s) and s[left] == s[right]:
                # 如果右指針減去左指針 + 1 的長度 > 目前最長的回文長度
                # If the length calculated as (right pointer - left pointer + 1) is greater than the current longest palindrome length.
                if right - left + 1 > self.max_length:
                    # 紀錄最長回文字串的起始位置
                    # Record the starting position of the longest palindromic substring
                    self.start = left
                    # 紀錄最長回文字串的長度
                    # Store the length of the longest palindromic substring
                    self.max_length = right - left + 1
                left -=1
                right +=1

        for i in range(len(s)):
            # Expand around a single character (odd-length palindrome)
            # Using only the single-character-centered expansion method, even-length palindromes(such as 'abba' and 'bb') will not be correctly identified.
            # 只用單字元為中心的擴展方法, 偶數長度的回文（如 "abba", "bb"）就不會被正確識別
            expand_around_center(i, i)


            # 只用雙字元為中心的擴展方法, 奇數長度的回文（如 "aba", "racecar", "madam"）就不會被識別
            # Using only the two-character-centered expansion method, odd- length, odd-length palindromes (such as 'aba', 'racecar', and 'madam') will not be correctly identified.
            # 同時處理兩種情況 才能找到所有可能的回文子字串。
            # Handling both cases simultaneously is necessary to find all possible palindromic substrings.
            # Expand around two adjacent characters (even-length palindrome)
            expand_around_center(i, i + 1)

        return s[self.start:self.start + self.max_length]


# @lc code=end

