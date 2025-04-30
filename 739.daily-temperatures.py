#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        # 取出temperatures的值和index
        for i, temp in enumerate(temperatures):
            # 當stack不是空的,且當前溫度大於stack的最後一個元素,表示找到比他溫度高的天
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 把stack的最後一個元素pop出來,表示找到比他溫度高的天
                # Pop the last element from stack, which represents the day with a higher temperature
                prev_index = stack.pop()
                # 計算之前還沒找到更高溫暫存的天,到現在的天數,算出總共幾天
                # Calculate the number of days since the previous day with a lower temperature 
                answer[prev_index] = i - prev_index
            # 溫度沒有比最後一個溫度高,把當前溫度的index加入stack
            #The temperature is not higher than the last temperature, add the current temperature's index to the stack 
            stack.append(i)

        return answer
        
# @lc code=end

