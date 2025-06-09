/*
 * @lc app=leetcode id=191 lang=cpp
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
class Solution
{
public:
    int hammingWeight(int n)
    {
        // int count = 0;
        // while (n > 0)
        // {
        //     // Extract the Least siginificant bit(LSB) of 'n' using bitwise AND with 1
        //     count += n & 1;
        //     // Right shift 'n' by 1 position.
        //     n >>= 1;
        // }
        // return count;

        // Brain Kernighan Algorithm
        int count = 0;
        while (n > 0)
        {
            // 5 -> 101 & 100 -> 100 & 011 -> 0, count -> 2
            n = n & (n - 1);
            count += 1;
        }
        return count;
    }
};
// @lc code=end
