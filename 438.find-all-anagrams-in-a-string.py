#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # # Brute-force approach
        # # This approach is inefficient and will likely cause a Time Limit Exceeded error on large inputs.
        # len_s,len_p = len(s),len(p)

        # if len_p > len_s:
        #     return []
        
        # result =[]

        # sorted_p = sorted(p)

        # # Iterate through all possible starting positions of a window in 's'
        # for i in range(len_s-len_p+1):
        #     substring = s[i:i+len_p]
        #     # Sorting the substring in every iteration is inefficient.
        #     if sorted(substring) == sorted_p:
        #         result.append(i)
        
        # return result

        # Sliding window + Frequency Counter

        len_s,len_p = len(s),len(p)

        if len_p>len_s:
            return []
        
        result =[]

        #Create frequency counters for p and the window, using arrays of size 26 for 'a'-'z'
        p_map = [0] * 26
        s_window = [0] * 26
        result = []
        ord_a = ord('a')
        # s = "cbaebabacd"

        # p = "abc"
        # Build the frequency counters for p and the initial window in s.
        for i in range(len_p):
            p_map[ord(p[i])-ord_a]+=1
            s_window[ord(s[i]) - ord_a] += 1
        
        #Check if the initial window is an anagram.
        if p_map == s_window:
            result.append(0)

        # Slide the window across the rest of s, one character at a time.
        for i in range(len_p,len_s):
            # Add the new character entering the window from the right.
            s_window[ord(s[i]) - ord_a] += 1
            # Remove the old character leaving the window from the left.
            s_window[ord(s[i-len_p]) - ord_a] -= 1

            if p_map == s_window:
                result.append(i-len_p+1)

        return result



        

        
# @lc code=end

