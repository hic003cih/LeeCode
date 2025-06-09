/*
 * @lc app=leetcode id=338 lang=cpp
 *
 * [338] Counting Bits
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution
{

public:
        vector<int> countBits(int n)
    {
        // DP
        // All elements are initially set to 0. ans[0] is set to 0. This allows the loop to start iterating from i = 1
        // vector<int> ans(n + 1, 0);
        // for (int i = 1; i <= n; i++)
        // {
        //     // i = 5 → 二進位 = 101
        //     // i >> 1 = 2 → 二進位 = 10
        //     // countBits[5] = countBits[2] + 1
        //     //  ans[i] = ans[i / 2] + (i % 2)
        //     ans[i] = ans[i >> 1] + (i & 1);
        // }
        // return ans;

        // Brute Force
        vector<int> ans(n + 1, 0);
        for (int i = 1; i <= n; i++)
        {
            ans[i] = count_ones(i);
        }
        return ans;
    }
    int count_ones(int x)
    {
        int count = 0;
        while (x)
        {
            count += x & 1;
            x >>= 1;
        }
        return count;
    }
};
// @lc code=end
