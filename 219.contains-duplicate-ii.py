#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # #Brute-force approach
        # # The method has a high time complexity(O(n*k))
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         # If the distance between indices exceeds k, no need to check further for this 'i'.
        #         if j - i > k:
        #             break
        #         #Check if the two numbers at these indices are identical
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # #Hash Map
        # #This approach uses a hash mp to achieve (O(n)) time complexity and (O(n)) space complexity
        # # This hash map will store the most recent index of each number encountered.
        # # {number: last_seen_index}
        # seem_map ={}
        # for i,num in enumerate(nums):
        #     # If the num is already in the map and the distance to its last occurrence is within k, we found a duplicate.
        #     if num in seem_map and i - seem_map[num] <= k:
        #         return True
        #     #add or update the last seen index for the current number to the hash map(key:num,value:i)
        #     # This prepares for future checks.
        #     seem_map[num] = i
        # return False

        # Sliding Window with Set
        #This approach achieves O(n) time complexity and O(k) space complexity 

        window_set = set()
        for i, num in enumerate(nums):
            if num in window_set:
                return True
            # Add the num to the window set for subsequent checks.
            window_set.add(num)

            # If the size of the window exceeds the k, remove the oldest element to maintain the window size.
            if len(window_set) > k:
                window_set.remove(nums[i-k])
        # If the loop completes, no such duplicate was found.
        return False
            
        
# @lc code=end

