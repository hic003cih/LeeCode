#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import math


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

        # # 使用單次遍歷
        # # 貪心演算法 Greedy Algorithm
        # # 每一步都選擇當下最優解
        # # 先遍歷一次,記錄最低的價格
        # # 再來遍歷剩下的全部的價格,減去最低的價格,得到最大利潤

        # # 設定一個很大的初始值
        # # Configure a large initial value
        # min_price = float('inf')
        # max_profit = 0

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     else:
        #         profit = price - min_price
        #         max_profit = max(max_profit, profit)
        
        # return max_profit

        #DP

        # if not prices:
        #     return 0
        
        # n = len(prices)

        # max_profit_sold= 0
        # min_cost_to_buy = -prices[0]

        # for i in range(1,n):
        #     # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     # dp[i][1] = max(dp[i-1][1], -prices[i])
        #     # 賣出股票最大利益 Max profit if we don't hold a stock at the end of day 'i'
        #     max_profit_sold = max(max_profit_sold, min_cost_to_buy + prices[i])
        #     # 找到最便宜的價格 Max profit if we hold a stock at the end of day 'i'
        #     min_cost_to_buy = max(min_cost_to_buy, -prices[i])
        # return max_profit_sold

        # #Brute-force approach
        # # This approach has a high time complexity and may exceed time limits

        # n = len(prices)
        # if n <2:
        #     return 0
        # max_profit = 0
        # # Outer loop: Iterates through each day 'i' as a potential buy day
        # for i in range (n):
        #     # Inner loop: Iterates through each day 'j' as a potential sale day
        #     #Iterate through the left price list
        #     # We must sale after buying, so 'j' start from 'i+1'
        #     for j in range (i+1,n):
        #         # Calculate the profit if we buy on day 'i' and sell on day 'j'
        #         profit = (prices[j]) - (prices[i]) 
        #         # If the profit greater than  pervious max_profit, update the max_profit value
        #         if profit >max_profit:
        #             max_profit = profit

        # return max_profit

        # Dynamic Programming
        
        n = len(prices)
        if n <2:
            return 0
        #Initialize a 2D DP array of size n * 2
        dp =[[0] * 2 for _ in range(n)]

        # Initialize the day '0' status
        # Maximum profit when holding no stock on day 0
        dp[0][0] = 0
        # Maximum profit or (minimum cost) when holding a stock on day 0
        dp[0][1] = -prices[0]

        # Iterate through the price list
        for i in range(1,n):
            # Calculate dp[i][0]: No stock in hand, and count the most profit
            # dp[i-1][0] is you do not have any stock yesterday
            # dp[i-1][1] + prices[i] is you have stock yesterday(dp[i-1][1]) and sold the stock today(the price is prices[i])
            # Choose the option that yields maximum profit
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            #Calculate dp[i][1]: Have stock in hand, and count the most profit
            # dp[i-1][1] is you have stock yesterday
            # -prices[i] is you want to buy stock today, and the price is prices[i] 
            # Choose the option that yields minimum cost
            dp[i][1] = max(dp[i-1][1], -prices[i])
        # Return the last day most profit when I sold stock 
        return dp[n-1][0]
        
        

        # # One-Pass Iteration, Greedy Algorithm
        # # Since a stock must be sold after it is bought, we only need to track the minimum price and continuously update the maximum profit based on the current price

        # if not prices or len(prices) < 2:
        #     return 0
        
        # #Initialize min_price to a infinity value to ensure min_price can set as the initial minimum.
        # min_price = float('inf')
        # max_profit = 0
        
        # # Iterate through the price list to find min_price and max_profit
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
            
        #     current_profit = price - min_price
            
        #     if current_profit > max_profit:
        #         max_profit = current_profit
        
        # return max_profit

        """
        :type prices: List[int]
        :rtype: int
        """
    # @lc code=end

