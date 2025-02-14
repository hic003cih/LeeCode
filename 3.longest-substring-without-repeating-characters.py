#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_length = 0

        # enumerate(iterable, start=0)
        # right is the index
        # char is the value
        for right, char in enumerate(s):

            # s = "abcabcbb"
            if char in char_index and char_index[char] >= left:
                # 如果有重複的字元,left index 往右邊移動
                left = char_index[char] + 1
            
            # 更新該字符最新的位置
            char_index[char] = right
            # 計算最大長度
            # {'a': 0, 'b': 1, 'c': 2}
            max_length = max(max_length, right - left + 1)

        return max_length
        
# @lc code=end

