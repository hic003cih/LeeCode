#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# Sliding window + HashMap
# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # arr = [2, 1, 5, 1, 3, 2]
        # s = "abcabcbb"

        char_set = set()
        left = 0
        max_length = 0

        # pwwkew
        # 右指針向右移動
        # Use the right pointer to traverse the string s.
        # for right in range(len(s)):
        #     # 如果右指針指到的字有在set中,表示重複了,將舊的left指針中存到的字移除,左指針的往右移
        #     # If the character at right pointer is already in the set, it means a duplicate is found. Remove the character stored at the old left pointer from the set and move the left pointer  to the right.
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     # 將右指針指到的字加入到set中
        #     # Insert the character at the right pointer into the set
        #     char_set.add(s[right])
        #     # 比較最大值
        #     # Compare the maximum value.
        #     max_length = max(max_length, right - left + 1)

        # return max_length

        # Sliding window + HashMap
        # left 起點, right 終點
        # left如果有重複的字移動到下一個位置
        # right 用來遍歷全部字串
        # 建立 Map char_index 紀錄每個字最後出現的位置
        # 曾出現移動left
        # s = "abcabcbb"
        # "pwwkew"

        # char_index = {}
        # left = 0
        # max_length = 0

        # for right in range(len(s)):
        #     # 找到重複的
        #     if s[right] in char_index and char_index[s[right]] >= left:
        #         # 找到重複的,移動左邊界
        #         left = char_index[s[right]] + 1

        #     # 更新當前位置
        #     char_index[s[right]] = right
        #     max_length = max(max_length, right - left + 1)

        # return max_length
        

        #arr = [2, 1, 5, 1, 3, 2]
        # s = "abcabcbb"

        # 用enumerate的方法去遍歷字串,並且獲取index
        # using enumerate method to traverse the string s and get the index
        for right, char in enumerate(s):
            # 如果char在char_index中,並且char_index的位置大於等於left表示
            # If char is in char_index and its position is greater than or equal to left
            if char in char_index and char_index[char] >= left:
                # 把left的index的位置+1
                # Move the left pointer to the next position
                left = char_index[char] + 1
            # 如果沒有在index中,則新增到char_index中
            # If char is not in char_index, add it to char_index
            char_index[char] = right
            # 計算最大長度
            # Calculate the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

        



        # char_index = {}
        # left = 0
        # max_length = 0

        # for right, left in enumerate(s):
        #     if char in char_index and char_index[char] >= left:
        #         left = char_index[char] + 1
            
        #     # {'a': 0}
        #     char_index[char] = right
        #     max_length = max(max_length, right - left + 1)

        # return max_length
        



        # char_index = {}
        # left = 0
        # max_length = 0

        # # enumerate(iterable, start=0)
        # # right is the index
        # # char is the value
        # for right, char in enumerate(s):

        #     # s = "abcabcbb"
        #     if char in char_index and char_index[char] >= left:
        #         # 如果有重複的字元,left index 往右邊移動
        #         left = char_index[char] + 1
            
        #     # 更新該字符最新的位置
        #     char_index[char] = right
        #     # 計算最大長度
        #     # {'a': 0, 'b': 1, 'c': 2}
        #     max_length = max(max_length, right - left + 1)

        # return max_length
        
# @lc code=end

