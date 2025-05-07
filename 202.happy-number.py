#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            # 先轉成字串,再轉成int,再平方,再相加
            # Convert n to a string, convert it to an int, square it, and add it
            n_str = str(n)
            # 建立存放平方的清單
            # Create a list to store the squares
            squares = []
            # 取出字元,轉成int並平方
            # Take out the characters, convert them to ints, and square them
            for c in n_str:
                digit = int(c)
                # 將int做平方,加入存放平方的清單
                # Square the int and add it to the list of squares
                squares.append(digit**2)
            # 把平方的清單相加
            # Add the list of squares
            n = sum(squares)
        return n == 1
        
# @lc code=end

