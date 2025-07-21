#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start

import heapq
from typing import List
from collections import Counter
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # # Brute-force Sorting
        # self.k = k
        # self.nums = nums

        # Min-Heap
        # Store k and initialize an empty min-heap.
        self.k = k
        self.min_heap = []

        #Process the initial numbers to establish the heap
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        # # Brute-force Sorting
        # # Add the new element to our list
        # self.nums.append(val)
        # # Sort the entire list every single time
        # self.nums.sort()
        # # Return the kth largest element
        # return self.nums[len(self.nums)-self.k]

        # Min-Heap
        # If the heap isn't full yet, just add the element.
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the new value is larger than the smallest element in heap (the root),
        # replace the smallest element with new value.
        elif val > self.min_heap[0]:
            #heapq.heapreplace is more efficient than a pop followed by a push. 
            heapq.heapreplace(self.min_heap, val)
        # Return the kth largest
        return self.min_heap[0]

        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

