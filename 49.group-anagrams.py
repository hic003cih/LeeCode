#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    from collections import defaultdict
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # anagram_map = {}
        anagram_map = defaultdict(list)

        for s in strs:
            # 排序字串，並轉為 tuple 作為 key
            # 字典的 key 必須是不可變（immutable）型別，但 sorted(s) 回傳的是 list，而 list 是可變的（mutable），不能作為字典的 key。
            sorted_key = tuple(sorted(s))

            # 如果 key 不存在，手動初始化
            # if sorted_key not in anagram_map:
            #     anagram_map[sorted_key] = []

            # 將字串加入對應的組
            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())
        


# @lc code=end

