#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        #ZZY
        # Z = result * 26 + value = 0 * 26 + 26 = 26
        # Z = result * 26 + value = 26 * 26 + 26 = 702
        # Y = result * 26 + value = 702 * 26 + 25 = 18277
        # result = result * 26 + value
        # result = ((D1 26^1 + D2) * 26^1) + D3 * 26^0
        # result = D1 * 26^2 + D2 * 26^1 + D3 * 26^0
        # 
        #ZZY -> 26 * 26 * 26 + 26 * 26 + 25 = 17576 + 676 + 25 = 18277
    result = 0
    for char in columnTitle:
        #Convert the character to its corresponding value
        # Excel 標題系統將字母 'A' 映射為 1
        # ord('A') - ord('A') = 65 - 65 = 0
        # 0 + 1 = 1
        value = ord(char) - ord('A') + 1
        # 'A' 映射為 1，但 AA 這個字母組合相當於 Excel 的第 27 列。
        # 這會在計算時依次處理每個字符，並依照位置進行加權（相當於 26 進位制的加法）。
        result = result * 26 + value
    return result


# @lc code=end

