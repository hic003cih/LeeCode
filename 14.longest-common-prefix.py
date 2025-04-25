#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
#strs = ["flower","flow","flight"]

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 如果strs是空,則直接結束
        # if not condition:
        # 當 condition 為 False 或等效於假值時執行的代碼
        if not strs:
            return ""
        
        # 先取第一個字串當假設答案
        # Start by assuming the first string as the common prefix
        prefix = strs[0]

        #跳過第一個index0的
        # Skip the first string
        for s in strs[1:]:

            #檢查"flow".startswith("flower") → False（因為 "flow" 比 "flower" 短）,所以縮短長度
            # "flow" doesn't start with "flower", so shorten the prefix
            while not s.startswith(prefix):
                # 刪除最後一個字
                # Remove the last character from the prefix
                prefix = prefix[:-1]
                #檢查完prefix是否有重複以後,如果為空了表示沒有重複
                # After checking the prefix is duplicated, if it is empty, it means there is no duplicate 
                if not prefix:
                    return ""
        #檢查完以後返回最長的prefix
        # After checking, return the longest prefix
        return prefix
        
# @lc code=end

