#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)

        # 最快的方法,如果字數一樣,則會回傳True
        # Fastest method if the number of characters is the same, it will return True
        return Counter(s) == Counter(t)
        
# @lc code=end

