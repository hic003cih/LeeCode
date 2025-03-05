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

        self.start, self.max_length = 0, 1  # 使用 self 變數來存儲


         # Function to expand around the center
        def expand_around_center(left, right):
            # 提醒系統這是一個 nonlocal 變數,在這個function中才可以使用
             #nonlocal start, max_length
             while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > self.max_length:
                    self.start = left
                    self.max_length = right - left + 1
                left -=1
                right +=1

        for i in range(len(s)):
            # Expand around a single character (odd-length palindrome)
            # 只用單字元為中心的擴展方法, 偶數長度的回文（如 "abba", "bb"）就不會被正確識別
            expand_around_center(i, i)


            # 只用雙字元為中心的擴展方法, 奇數長度的回文（如 "aba", "racecar", "madam"）就不會被識別
            # 同時處理兩種情況 才能找到所有可能的回文子字串。
            # Expand around two adjacent characters (even-length palindrome)
            expand_around_center(i, i + 1)

        return s[self.start:self.start + self.max_length]


# @lc code=end

