#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
from collections import defaultdict
from collections import Counter

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # # Brute-force approach
        # # This Method has a high time complexity (O(N^3)) and is prone to Time Limit Exceeded(TLE) errors for larger inputs.
        
        # # If the lengths of the strings are different, they cannot be anagrams. Return False immediately.
        # if len(s)!=len(t):
        #     return False
        # # Convert string 's' to a list of characters to allow in-place removal of matched elements.
        # s_list = list(s)

        # # outer loop:Iterate through each character in string 't'
        # for char_t in t:
        #     found = False
        #     # inner loop: search for the current character from 't' within the remaining characters of 's_list'
        #     for i in range(len(s_list)):
        #         if s_list[i] == char_t:
        #             # if a match is found, remove the the character from s_list
        #             s_list.pop(i)
        #             found = True
        #             # Break the inner loop and proceed to the next character in 't'
        #             break
        #     # If no matching character is found in s_list after checking all its elements, 's' cannot be an anagram of 't'.
        #     if not found:
        #         return False
        # # If the outer loop completes, it means all characters in 't' found a match in 's'
        # # For 's' and 't' to be anagrams, s_list must now be empty.
        # # Return True if s_list is empty (meaning all characters from s were matched), False otherwise.
        # return not s_list

        # # Sorting

        # # If the lengths of the strings are different, they cannot be anagrams. 
        # if len(s) != len(t):
        #     return False
        # # Convert strings to sorted lists of characters for comparison.
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # return sorted_s == sorted_t

        # # Hash map
        # # If the lengths of the strings are different, they cannot be anagrams
        # if len(s) != len(t):
        #     return False
        # # Initialize a dictionary(hash map) to store character frequencies.
        # char_counts = defaultdict(int)

        # # First Pass: Populate the frequency map with characters from string 's'
        # for char in s:
        #     char_counts[char] +=1

        # # Second Pass: Decrement counts for characters found in string 's'
        # for char in t:
        #     # You must minus one in dictionary first, because visit not exist number in dictionary, it will give it zero number
        #     char_counts[char] -=1
        #     if char_counts[char] < 0:
        #         return False
        # # final check: after processing 't', all character counts in the map must be zero.
        # for count in char_counts.values():
        #     if count !=0:
        #         return False
        # return True

        # # Array Counting
        # # Most optimitzed method

        # if len(s) != len(t):
        #     return False
        # # Intialize an array in size 26, store a to z character
        # counts = [0] * 26
        # # ord('a')  ASCII is 97
        # offset_a = ord('a')

        # # Iterate through s, increase counts of each character
        # for char_s in s:
        #     # ex. ord('b')  ASCII is 98,  98-97=1, index = 1 is b.
        #     index = ord(char_s) - offset_a
        #     counts[index] +=1
        
        # for char_t in t:
        #     index = ord(char_t) - offset_a
        #     counts[index] -=1

        #     if  counts[index] < 0:
        #         return False
        # return True

        # collections.Counter
        # Counter(s) 會將字串 s 轉換為一個字元計數的字典 (Counter 物件)
        # 直接比較兩個 Counter 物件是否相等即可
        return Counter(s) == Counter(t)

        
# @lc code=end

