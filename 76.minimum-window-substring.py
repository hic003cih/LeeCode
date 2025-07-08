#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
import collections
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
    #     #Brute-force approach
    #     # This approach is inefficient and will likely cause a Time Limit Exceeded(TLE) error on large inputs

    #     # Create a frequency map (dictionary) for the characters in the target string 't'.
    #     # This map will be used to validate substrings from 's'.
    #     t_counts ={}
    #     #Create a frequency map for the characters in the t string
    #     for char in t:
    #         t_counts[char] = t_counts.get(char,0)+1
        
    #     min_len = float('inf')
    #     result = ""
    #     n = len(s)

    #     # Step 1:Generate all possible substrings
    #     for i in range(n):
    #         # Fix i index and iterate through all remaining characters
    #         for j in range(i,n):
    #             substring = s[i:j+1]
    #             # Step 2: For each substring, check if it is a valid window.
    #             if self.is_valid(substring,t_counts):
    #                 # Step 3 : If the substring is valid and shorter than the current minimum, update the result.
    #                 if len(substring) < min_len:
    #                     min_len = len(substring)
    #                     result = substring
    #     return result

                
    # def is_valid(self, sub:str, t_counts:dict) -> bool:
    #     # A simple optimization
    #     # the length of the substring must be greater than or equal to the total count of required characters.
    #     if len(sub) < sum(t_counts.values()):
    #         return False
    #     # Create a frequency map for the characters in the substring.
    #     sub_counts ={}
    #     # Iterate through each character in the substring.
    #     for char in sub:
    #         # Increment the frequency count for the given character.
    #         # Get the current count (defaulting to 0 if not present) and increment it.
    #         sub_counts[char] = sub_counts.get(char,0)+1
    #      #Iterate through each character and its required count in t_counts.
    #     for char,count in t_counts.items():
    #         # If the substring has fewer instances of a character than required, it's invalid.
    #         if sub_counts.get(char,0) < count:
    #             return False
    #     return True

    # #Sliding Window
    #  # Frequency map for characters in t
    #     # t 中字元的頻率表
    #     need = collections.Counter(t)
        
    #     # Frequency map for characters in the current window
    #     # 當前窗口中字元的頻率表
    #     window = collections.defaultdict(int)

    #     left, right = 0, 0
        
    #     # 'valid' tracks how many unique characters in t are satisfied in the current window.
    #     # 'valid' 用於追蹤當前窗口滿足了 t 中多少個獨立字元的需求。
    #     valid = 0
        
    #     # Start index and length of the minimum window found so far.
    #     # 到目前為止找到的最小窗口的起始索引和長度。
    #     start = 0
    #     min_len = float('inf')

    #     while right < len(s):
    #         # c is the character being added to the window
    #         # c 是即將要移入窗口的字元
    #         c = s[right]
    #         right += 1
            
    #         # --- Expand the window ---
    #         # --- 擴大窗口 ---
    #         if c in need:
    #             window[c] += 1
    #             if window[c] == need[c]:
    #                 valid += 1

    #         # --- Shrink the window when a valid window is found ---
    #         # --- 當找到一個有效的窗口時，開始收縮 ---
    #         while valid == len(need):
    #             # Update the minimum window size if the current one is smaller
    #             # 如果當前窗口更小，就更新最小窗口的紀錄
    #             if right - left < min_len:
    #                 start = left
    #                 min_len = right - left
                
    #             # d is the character being removed from the window
    #             # d 是即將要移出窗口的字元
    #             d = s[left]
    #             left += 1

    #             # --- Update window counts after removal ---
    #             # --- 移除後更新窗口內的計數 ---
    #             if d in need:
    #                 # This check is crucial. We only decrement 'valid' when the count
    #                 # of a required character drops below its needed frequency.
    #                 # 這個檢查至關重要。只有當一個必要字元的計數
    #                 # 從「滿足」變為「不滿足」時，我們才將 'valid' 減一。
    #                 if window[d] == need[d]:
    #                     valid -= 1
    #                 window[d] -= 1

    #     return "" if min_len == float('inf') else s[start:start + min_len]

        #Slightly Optimized Sliding Window

        if not t or not s:
            return ""
        
        #Frequency map for characters in t
        need = collections.Counter(t)

        #The total number of characters we need to find in a window.
        required_chars = len(t)

        left = 0
        min_len = float('inf')
        start_index = 0

        for right,char in enumerate(s):
            #If the current character is needed, decrement the required count.
            # A count > 0 in 'need' means this character is still required.
            if need[char] > 0:
                required_chars -= 1
            #Decrement the count for the current character. If its' not in t,
            #its count will become negative, indicating an excess
            need[char] -=1

            # When required_chars becomes 0, we have a valid window.
            # Time to shrink it from the left.
            while required_chars==0:
                # Update our result if we've found a new minimum window.
                current_len =right - left +1
                if current_len < min_len:
                    min_len = current_len
                    start_index = left
                # Start shrinking the window by moving the left pointer.
                left_char =s[left]

                # The character at 'left' is leaving the window, so we increment its count in 'need'.
                need[left_char] +=1

                # If the count of left_char becomes positive, it means this character
                # is now required for a valid window.

                if need[left_char] > 0:
                    required_chars +=1
                
                left +=1
        return "" if min_len == float('inf') else s[start_index:start_index + min_len]

    
# @lc code=end
