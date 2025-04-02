#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 額外陣列

        # n = len(nums)
        # res = [0] * n
        # for i in range(n):
        #     res[(i + k) % n] = nums[i]
        # # 因為題目要求要使用原本的nums,把 res 的所有內容，複製到 nums 原陣列裡面（就地修改）
        # nums[:] =res

        # Python切片(短的)
        # nums = [1,2,3,4,5,6,7]
        # k = 3
        # nums[-3:]   = [5,6,7]
        # nums[:-3]   = [1,2,3,4]
        # 會用到額外空間,建立「兩個新的切片」，然後再把它們串接成一個新的 list。

        # k %= len(nums)
        # nums[:] = nums[-k:] + nums[:-k]

        # 三次翻轉法（in-place O(1) 空間）
        # 不需要用到額外的空間
        # 反轉整個陣列
        # 反轉前 k 個元素
        # 反轉剩下的 n-k 個元素
        
        n = len(nums)
        # 處理 k > n 的情況（如果要移動的數量大於陣列的長度,多繞一圈等於沒轉,所以先除以陣列的長度,剩下的再做處裡）
        k %= n

        def reverse(start, end):
            # 雙指針對換
            while start < end:
                # 指針位置對調
                # 左指針慢慢往前,右指針慢慢往後,兩個指針重疊以後停止
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 反轉整個陣列
        reverse(0, n - 1)
        # 前 k 個轉正
        reverse(0, k - 1)
        # 剩下的K個也轉正
        reverse(k, n - 1)




# @lc code=end

