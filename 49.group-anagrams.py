#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# 哈希分組 + 排序
# @lc code=start
class Solution(object):
    from collections import defaultdict
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # # 排序法
        # # anagram_map = {}
        # anagram_map = defaultdict(list)

        # for s in strs:
        #     # 排序字串，並轉為 tuple 作為 key
        #     # 字典的 key 必須是不可變（immutable）型別，但 sorted(s) 回傳的是 list，而 list 是可變的（mutable），不能作為字典的 key。
        #     sorted_key = tuple(sorted(s))

        #     # 如果 key 不存在，手動初始化
        #     # if sorted_key not in anagram_map:
        #     #     anagram_map[sorted_key] = []

        #     # 將字串加入對應的組
        #     anagram_map[sorted_key].append(s)

        # return list(anagram_map.values())


        # 用字母計數表當作 Key
        # Using letter count table as key
        anagrams = defaultdict(list)


        # for word in strs:
        #    # 26 個小寫英文字母,所以要產生26長度的陣列
        #    # Create an array of length 26 to count each letter
        #     count = [0] * 26
        #     for c in word:
        #         # 把字元變成ASCII,減去a的ASCII,因為結果會少1,所以還要再加1,才能變成對應0-25 並且對應到陣列 ex -> a =97, c = 99, c -a = 2
        #         # transfer letter to ASCII, minus a's ASCII, because the result will be less 1, then add 1, it will become 0 -25 and correspond to the array
        #         # Map the character to an index from 0 to 25
        #         count[ord(c) - ord('a')] += 1
        #     # list 不可作為 dictionary 的 key，tuple 才可以
        #     # lists are unhashable and cannot be used as dictionary keys, but tuples can be used as keys
        #     key = tuple(count)
        #     # 將字串加入對應的組
        #     # Add the string to corresponding group
        #     anagrams[key].append(word)

        # # 將所有字串列表取出,轉成 list回傳
        # # Return all grouped anagrams as a list
        # return list(anagrams.values())

        for c in strs:
            count = [0] * 26
            for l in c:
                count[ord(l) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(c)
        
        return list(anagrams.values())


# @lc code=end

