#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):

    from collections import Counter
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums = [1,1,1,2,2,3], k = 2

        # heap（小頂堆）
        # count = Counter(nums)
        # return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

        # Bucket Sort
        # 計算每個數字出現的頻率
        # Count the frequency of each number
        # count = {1:3, 2:2, 3:1}
        count = Counter(nums)

         # 初始化桶子,建立一個長度為 nums + 1 的陣列
         # Initialize buckets, create an array of length nums + 1
        # freq[1] = [3], freq[2] = [2], freq[3] = [1]
        freq = [[] for _ in range(len(nums) + 1)]
         # count = {1:3, 2:2, 3:1}
         # freq[1] = [3], freq[2] = [2], freq[3] = [1]
        for num, c in count.items():
            freq[c].append(num)

        # 找出前 K 個出現次數最多的元素
        # Find the top K most frequent elements
        res = []
        # 掃 freq 陣列的 index,從最大的index往下數,到最小的index(freq[1]), ex. range(6, 0, -1) 從6到0,每次減一
        # Scan the index of freq array from largest to smallest, ex. range(6, 0, -1) from 6 to 0, each time minus 1
        for i in range(len(freq) -1 , 0, -1):
            # 將該頻率的元素加入結果res中
            # Add the elements of the corresponding frequency to res
            for num in freq[i]:
                # 將num加入res中
                # Add num to res
                res.append(num)
                # 如果長度到達k,則直接返回結果
                # If the length reaches k, return the result
                if len(res) == k:
                    return res

        

        
# @lc code=end

