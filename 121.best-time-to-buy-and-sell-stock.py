#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        # 表示無窮大,為了第一個可以直接更新
        min_price = float('inf')
        max_profit = 0
#  Input: prices = [7, 1, 5, 3, 6, 4]
        for price in prices:
            #要找大最大利潤,將買入的價格最便宜的值存起來
            if price < min_price:
                min_price = price
            #當買入的價格是最小值存起來,計算當前的價格和買入的價格是否為最大利潤
            elif price - min_price > max_profit:
                    max_profit = price - min_price

        return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        
# @lc code=end

