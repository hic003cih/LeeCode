#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq

class Solution(object):

    from collections import Counter
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums = [1,1,1,2,2,3], k = 2

        # #1. Brute-force
        # # Step1:Count the frequency of each number.
        # freq_map = Counter(nums)

        # # Step2: Sort the items by frequency in descending order.
        # sorted_items = sorted(freq_map.items(), key = lambda item:item[1],reverse=True)

        # #Step3:Extract the top k elements.
        # result = [item[0] for item in sorted_items[:k]]

        # return result

        # #2. Min-Heap
        # #Step1: Count frequencies.
        # if k == len(nums):
        #     return nums
        # freq_map = Counter(nums)
        # #Use a min-heap to find the top k frequent elements.
        # min_heap =[]
        # for num, freq in freq_map.items():
        #     heapq.heappush(min_heap, (freq, num))
        #     # If the heap size exceeds k, pop the element with the smallest frequency.
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        # # Extract the numbers from the heap.
        # return [item[1] for item in min_heap]

        # 3. Bucket Sort
        # Count frequencies of each number.
        freq_map = Counter(nums)

        # Create buckets where the index represents frequency.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Populate the buckets. where m is unique elements.
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Iterate through buckets from highest frequency to lowest.
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result




        
# @lc code=end

