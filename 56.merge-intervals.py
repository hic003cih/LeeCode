#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
# Greedy Algorithm

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 先講list排序
        intervals.sort(key= lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果merged是空的
            # merged[-1][1]：merged 裡 最後一個區間的結束end時間
            # 如果前一個區間的 end 比當前區間的 start 還小
            # 代表沒有重疊, 直接append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 有重疊, 將當前區間的end更新為較大的end,合併成一個區間(list)
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

        # # [[3,5], [1,4], [2,6]]
        # # Bubble sort
        # # 迴圈比較每個值,不適合大規模資料
        # n = len(intervals)
        # for i in range(n):
        #     # 最後一個數一定是最大的,所以可以不用比較
        #     # i=0時比較全部,所以不會有沒比較到的問題
        #     for j in range(n-i-1):
        #         if intervals[j][0] > intervals[j+1][0]:
        #             intervals[j][0], intervals[j+1] = intervals[j+1][0], intervals[j][0]
        #     return intervals

            # # 選擇排序法  (Selection Sort)
            # # 從未排序的值之中選最小值,放到排序好的部分中
            # # 效率比bubble sort好一點
            # n = len(intervals)
            # for i in range(n):
            #     #用來記錄還沒處理過的數值中最小元素的索引
            #     min_index = i
            #     # 在剩餘元素中尋找最小值
            #     for j in range(i +1, n):
            #         if intervals[j][0] < intervals[min_index][0]:
            #             min_index = j 
            #     # 結束迴圈後,交換最小值到已排序的部分
            #     intervals[i], intervals[min_index] = intervals[min_index], intervals[i]
            # return intervals  
            
            # # 快速排序（Quick Sort）
            # # 分治法 (Divide and Conquer) 的排序演算法
            # # 選一個基準點(pivot), 然後將陣列分成小於,等於,大於三個部分
            # # 對小於大於的部分做遞迴排序, 等於的部分不做排序
            # # 合併三個部分
            # def quick_sort(intervals):
            #     # 如果長度不用繼續比較大小,回傳intervals並且回溯
            #     if len(intervals) <=1:
            #         return intervals
                
            #     # 找到pivot
            #     pivot = intervals[len(intervals) // 2]
            #     left = [x for x in intervals if x <pivot]
            #     middle = [x for x in intervals if x == pivot]
            #     right = [x for x in intervals if x > pivot]
            #     #最底層的 left 和 right 先合併，然後逐層向上合併
            #     return quick_sort(left) + middle + quick_sort(right)

            
        
# @lc code=end

