#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#
#Input: haystack = "sadbutsad", needle = "sad"
#Output:0
# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n ==0:
            return 0 #Empty needle is always found at index 0

        # Sliding window
        # 為了不超出needle的長度,最多只循環到
        # range(8 - 5 + 1) = range(4)，即索引 0 到 3
        # To stay within the bounds of needle, loop up to range(8 -5 + 1), range(4), which covers index 0 to 3
        for i in range(m-n+1):
            # 比較子字串的長度與needle是否相等
            #Compare substring of length n with needle
            # leetcode -> haystack[0:5] = "leetc" -> index 0~4
            if haystack[i:i + n] ==needle:
                return i

        return -1
        

# @lc code=end

