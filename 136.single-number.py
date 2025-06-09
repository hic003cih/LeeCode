#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# a=4 的二進制表示為 100ll

# b=1 的二進制表示為 001
# @lc code=start

from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        result = 0
        # Iterate through each number in the input array
        for num in nums:
            # Performs a bitwise XOR operation to find the number to find answer. ex. 3 xor 2 -> 01, 01 xor 2 -> 3(11)
            #result = result ^ num
            # result = 0 ^ 4 = 4  
            # result = 4 ^ 1 = 5
            # result = 5 ^ 2 = 7
            # result = 7 ^ 1 = 6
            # result = 6 ^ 2 = 4
            result ^= num
        return result

        # Hash_Map
        #Initialize a dictionary to store the frequency of each number.
        # Key: the number itself, Value:its count
        # count_Map = {}
        # count_Map = defaultdict(int)
        
        # # Iterate through the number in the list to populate the frequency map.
        # for num in nums:
        #     # If the number is already in the map, increment its count.
        #     # count_Map[num] =count_Map.get(num, 0) + 1
        #     count_Map[num] += 1
            
        # # Iterate through the frequency map to find the number with a count of 1, return the number to be the answer
        # for index,value in count_Map.items():
        #     if value==1:
        #         return index
            
                
        # return 0
# @lc code=end

