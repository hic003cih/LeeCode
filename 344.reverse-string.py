#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseHelper(self,s: List[str],left:int,right:int) -> None:
        if (left >= right):
            return
        s[left],s[right] = s[right],s[left]
        self.reverseHelper(s,left+1,right-1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # #Recursion approach
        # self.reverseHelper(s,0,len(s)-1)

        #Two-Pointer
        left = 0
        right = len(s)-1
        while(left < right):
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

    
        
        

        
# @lc code=end

