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
        
        
        prefix = strs[0]

        #跳過第一個index0的
        for s in strs[1:]:

            #檢查"flow".startswith("flower") → False（因為 "flow" 比 "flower" 短）,所以縮短
            while not s.startswith(prefix):
                # 刪除最後一個字
                prefix = prefix[:-1]
                #檢查完prefix是否有重複以後,如果為空了表示沒有重複
                if not prefix:
                    return ""
        #檢查完以後返回最長的prefix
        return prefix
        
# @lc code=end

