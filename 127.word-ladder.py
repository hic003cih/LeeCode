#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)

        # 如果結束字不在字典裡,直接回傳0
        if endWord not in wordList:
            return 0
        
        # 使用 list 當 queue，格式是 (單字, 深度)
        # Use list as queue, format is (word, depth)
        queue = [(beginWord, 1)]

        while queue:
            current_word, depth = queue[0]
            # 等同於 deque.popleft()
            # Equivalent to deque.popleft()
            queue = queue[1:]

            # 遍歷當前單字的每個字元
            # Traverse each character of the current word
            for i in range(len(current_word)):
                # 遍歷所有字母
                # Traverse all letters
                for c in "abcdefghijklmnopqrstuvwxyz":

                    # 前面部分（不包含 i） + 新字元 + 後面部分（不包含 i）
                    # Front part (not including i) + new letter + back part (not including i)
                    new_word = current_word[:i] + c + current_word[i+1:]

                    # 如果新單字等於結束單字,直接回傳深度 + 1
                    # If the new word is equal to the end word, directly return the depth + 1
                    if new_word == endWord:
                        return depth + 1
                    # 如果新單字在字典裡,將新單字加入queue中
                    # If the new word is in the dictionary, add it to the queue
                    if new_word in wordSet:
                        # 從wordSet中刪除,避免重複
                        # Delete from wordSet to avoid duplication
                        wordSet.remove(new_word)
                        # 將新單字加入queue中,並將深度加1
                        # Add the new word to the queue and increase the depth
                        queue.append((new_word, depth + 1))
        return 0

        

        

        
        
# @lc code=end

