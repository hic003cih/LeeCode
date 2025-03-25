#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
#Binary Search
# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_position(is_first):
           left, right = 0, len(nums) - 1
           # 如果沒找到,返回-1
           # If not found, return -1
           position = -1


           while left <= right:
            # 計算中間索引
            # Calculate the middle index
            mid = (left + right) // 2

            # 如果找到了target
            # If found the target value
            if nums[mid] == target:
                position = mid
                # 因為要找最左跟最右邊的,有可能是好幾個一樣的數字排在一起,所以要繼續往左右找
                # Because we want to find the leftmost or rightmost index, we need to continue searching in that direction.
                # 如果是搜尋第一個出現的值,往左邊找位置
                # If we want to search for the first occurrence of the value, we need to continue searching the leftmost position
                if is_first:
                    right = mid - 1
                else:
                # 如果是最後一個出現的值,往右邊的位置找
                # If we want to search for the last occurrence of the value, we need to continue searching the rightmost position
                    left = mid +1
            # 如果比target小,移動到右半邊
            # If the value < target, move to the right
            elif nums[mid] < target:
                left = mid + 1
            # 如果比target大,移度到左半邊
            # If the value > target, move to the left
            else:
                right = mid - 1
           return position



        # def find_position(is_first):
        #     left, right = 0, len(nums) -1
        #     position = -1
            
        #     while left <= right:
        #             mid = (left + right) // 2

        #             if nums[mid] == target:
        #                 position = mid #Possible first/last position
        #                 if is_first:
        #                     right = mid - 1 # Continue searching left for first occurrence
        #                 else:
        #                     left = mid + 1 # Continue searching right for last occurrence
        #             elif nums[mid] < target:
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #     return position


        first = find_position(True) #Find first occurrence
        last = find_position(False) # FInd last occurrence

        return [first, last]
            
        
        
# @lc code=end

