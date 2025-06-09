/*
 * @lc app=leetcode id=231 lang=cpp
 *
 * [231] Power of Two
 */

// @lc code=start
class Solution
{
public:
    bool isPowerOfTwo(int n)
    {
        bool result = false;
        // 如果 n 是 2 的冪，它的二進位只有一個 1
        // If n is a power of 2, its binary representation has only one '1', ex. 1000(8)
        // 減去 1 之後，會把那個 1 變成 0，而 1 右邊全部變成 1
        // After subtracting 1 from n, that '1' bit becomes '0', and all bits to its right become '1'.
        // n & (n - 1) 會剛好變成 0
        // Therefore, n & (n - 1) will be 0. ex. 1000(8) & 0111(7) = 0

        // if (n > 0)
        // {
        //     result = (n & (n - 1)) == 0;
        // }
        // return result;

        if (n < 0)
            return false;
        while (n % 2 == 0)
        {
            n = n / 2;
        }
        return n == 1;
    }
};
// @lc code=end
