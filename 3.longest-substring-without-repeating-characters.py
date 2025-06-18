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

    #     # Brute-force approach
    #     # this approach might exceed time limits for very large inputs
    #     # Outside circle
    #     for i in range(len(s)):
    #         # Inside circle
    #         for j in range(i,len(s)):
    #             # get the current string
    #             current_substring = s[i:j+1]
    #             #Modularity
    #             # Check the current string has repeat chars
    #             if self._has_no_repeating_chars(current_substring):
    #                 # If it has no repeating chars, update the maxlength
    #                 max_length = max(max_length, len(current_substring))
        
    #     return max_length

    
    # def _has_no_repeating_chars(self, substring):


    #     char_set = set()
    #     # Iterate through the substring
    #     for char in substring:
    #         # If the character already exists in the set
    #         if char in char_set:
    #             return False
    #         # If it does not exist, add the character to the hash_set
    #         char_set.add(char)
    #     return True



        # # Brute-force approach(optimized)
        # # 
        # n = len(s)
        # if n ==0:
        #     return 0

        # # Outside circle
        # for i in range(n):
        #     # Using set to store used characters
        #     char_set = set()
        #     # Inside circle
        #     for j in range(i,n):
        #         # process the current character
        #         char = s[j]
        #         # If the current character already exist in the used characters set, break the inner loop
        #         if char in char_set:
        #             break
        #         else:
        #             # If the current character not in the set, append the character in the set
        #             char_set.add(char)
        #             # update the maximum length. The length of the current non-repeating is (j - i + 1)
        #             max_length = max(max_length, j-i+1)
        
        # return max_length
    
        # Sliding window
        n=len(s)
        if n==0:
            return 0
        
        # Initialize the left pointer
        left = 0
        # Initialize the set to stored the used characters
        char_set = set()

        # Iterate through the string
        for right in range(n):
            # Store the current character
            current_char = s[right]
            # If the current character exists in the used characters set
            # It means the current_char is already present within the current window s[left:right]
            # Therefore, we need to shrink the window from the left
            # until the current_char is not exists in the used characters set
            while current_char in char_set:
                char_set.remove(s[left])
                left +=1

            char_set.add(current_char)

            max_length = max(max_length, right - left +1)

        return max_length


        
# @lc code=end

