#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
#         # 表示無窮大,為了第一個可以直接更新
#         min_price = float('inf')
#         max_profit = 0
# #  Input: prices = [7, 1, 5, 3, 6, 4]
#         for price in prices:
#             #要找大最大利潤,將買入的價格最便宜的值存起來
#             if price < min_price:
#                 min_price = price
#             #當買入的價格是最小值存起來,計算當前的價格和買入的價格是否為最大利潤
#             profit = price - min_price
#             if profit > max_profit:
#                     max_profit = profit

#         return max_profit

        # 暴力法
        # 可以得出解,但會超時
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         # 找出價差最大的
        #         max_profit = max(max_profit, prices[j] - prices[i])
        # return max_profit

        # 使用單次遍歷
        # 貪心演算法 Greedy Algorithm
        # 每一步都選擇當下最優解
        # 先遍歷一次,記錄最低的價格
        # 再來遍歷剩下的全部的價格,減去最低的價格,得到最大利潤

        # 設定一個很大的初始值
        # Configure a large initial value
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # 買入價一定發生在賣出價之前
            min_price = min(min_price, price)
            # 賣出價 - 買入價
            max_profit = max(max_profit, price - min_price)
        return max_profit

        
        """
        :type prices: List[int]
        :rtype: int
        """
        
# @lc code=end

