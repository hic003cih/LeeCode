#include <vector>
#include <unordered_map> // also include this for unordered_map

using namespace std; // or use std::vector instead

/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> num_map;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];

            if (num_map.find(complement) != num_map.end())
            {
                result = {num_map[complement], i};
                return result;
            }
            num_map[nums[i]] = i;
        }
        return result;
    }
};
// @lc code=end
