/*
 * @lc app=leetcode id=136 lang=cpp
 *
 * [136] Single Number
 */

#include <unordered_map>
#include <vector>
#include <stdexcept>
using namespace std;

// @lc code=start
class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        // XOR function
        if (nums.empty())
        {
            throw std::invalid_argument("Input array 'nums' cannot be empty for singleNumber problem.");
        }
        // 選定第一個數來和剩餘的數做xor運算
        int ans = nums[0];
        // Iterate through all numbers in the array, to find the number that appears only once.
        for (int i = 1; i < nums.size(); i++)
        {
            // XOR「兩位不同」時，才會是 1
            // XORing two different bits results in '1'.
            //  2 ^ 1 = 3 -> 10 ^ 01 = 11
            //  7 ^ 5 = 2 -> 111 ^ 101 = 010
            //  每一對出現兩次的數字 XOR 起來會變成 0
            //   every pair of identical numbers in the array will XOR out to '0'
            //   ans = ans ^ nums[i];
            ans ^= nums[i];
        }
        return ans;

        // Hash_map
        // unordered_map<int, int> count_map;

        // // 第一次迴圈：先統計每個數字出現次數
        // // num 是value值
        // for (int i = 0; i < nums.size(); i++)
        // {
        //     count_map[nums[i]]++;
        // }
        // // 第二次迴圈：找出只出現一次的數字
        // // auto&自動推斷型別，加上 & 表示用「參考（reference）」避免拷貝
        // // pair 是value值
        // for (auto &pair : count_map)
        // {
        //     // pair.first 是 map 的 key, pair.second 是 value
        //     if (pair.second == 1)
        //     {
        //         return pair.first;
        //     }
        // }
        // return 0;
    }
};
// @lc code=end
