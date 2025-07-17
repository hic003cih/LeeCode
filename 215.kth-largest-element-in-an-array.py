#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # 1. Sorted
        # # Sort the array in ascending order.
        # nums.sort()
        # return nums[len(nums) - k]

        # #2. Min-Heap
        # #Create an empty min-heap.
        # min_heap = []
        # nums = [3, 2, 1, 5, 6, 4]
        # for num in nums:
        #     # Push the current element onto the heap.
        #     # The smallest number will be at the top.
        #     heapq.heappush(min_heap,num)
        #     # If the heap size is greater than k, remove the smallest element.
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        # # The root of the heap is the k-th largest element.
        # return min_heap[0]

        # 3. Quick select
        # nums = [3, 2, 1, 5, 6, 4]
        target_index = len(nums) - k
        left,right = 0, len(nums) -1

        while left <= right:
            #Choose a radom pivot to avoid worst-case O(n^2) performance.
            pivot_index = random.randint(left, right)
            #Partition the array and get the final position of the pivot.
            final_pivot_index = self.partition(nums, left, right,pivot_index)

            if final_pivot_index == target_index:
                return nums[final_pivot_index]
            elif final_pivot_index < target_index:
                left = final_pivot_index + 1
            else:
                right = final_pivot_index - 1
    def partition(self, nums: List[int], left: int, right: int, pivot_index:int) -> int:
        pivot_value = nums[pivot_index]
        # Move pivot to the end.
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final sorted position.
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        return store_index


# @lc code=end

