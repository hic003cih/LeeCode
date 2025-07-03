/*
 * @lc app=leetcode id=3 lang=c
 *
 * [3] Longest Substring Without Repeating Characters
 */

#include <stdbool.h>
#include <string.h>
// @lc code=start
bool allUnique(const char *s, int start, int end)
{
	// 使用一個大小為 128 的整數陣列來模擬一個雜湊集合 (Set)。
	// 為何是 128？因為標準的 ASCII 字元集正好有 128 個字元 (從 0 到 127)。
	//`{0}` 的意思是將陣列中所有 128 個位置的值都初始化為 0。
	int set[128] = {0};
	for (int i = start; i < end; i++)
	{
		int c = s[i];
		if (set[c] > 0)
		{
			return false;
		}
		set[c]++;
	}
	return true;
}
int max(int a, int b)
{
	// If a > b return a, or b
	return a > b ? a : b;
}
int lengthOfLongestSubstring(char *s)
{
	// Brute-force approach
	// int n = strlen(s);
	// int maxLength = 0;
	// for (int i = 0; i < n; i++)
	// {
	// 	for (int j = i; j < n; j++)
	// 	{
	// 		if (allUnique(s, i, j + 1))
	// 		{
	// 			if (j - i + 1 > maxLength)
	// 			{
	// 				maxLength = j - i + 1;
	// 			}
	// 		}
	// 	}
	// }
	// return maxLength;

	// Sliding Window+set
	// int n = strlen(s);
	// if (n == 0)
	// 	return 0;
	// // Assume ASCII character set (128 characters)
	// bool set[128] = {false};

	// int maxLength = 0;
	// int left = 0, right = 0;

	// while (right < n)
	// {
	// 	char char_right = s[right];
	// 	// If the current character is already in the window, shrink the window from the left.
	// 	// until the duplicate is removed.
	// 	while (set[char_right] == true)
	// 	{
	// 		// Mark the character at the 'left' pointer as out of the window
	// 		set[s[left]] = false;
	// 		left++;
	// 	}
	// 	// Add the current character to the window.
	// 	set[char_right] = true;
	// 	// Update the maximum length found so far.
	// 	maxLength = max(maxLength, right - left + 1);
	// 	// Move the right pinter to find maxLength substring
	// 	right++;
	// }
	// return maxLength;

	// Sliding window + HashMap
	int n = strlen(s);
	int maxLength = 0;

	// Use array as a hash map map[char] -> index
	//  Initialize the value as -1
	int map[128];
	for (int i = 0; i < 128; i++)
	{
		map[i] = -1;
	}

	int left = 0;
	for (int right = 0; right < n; right++)
	{
		char char_right = s[right];

		// Check if the character has been seen before, and its last occurrence is within the current window(right - left + 1)
		if (map[char_right] >= left)
		{
			// Move the left pointer to the position right after the last occurrence of the duplicate character.
			left = map[char_right] + 1;
		}
		// Update the character's newest index
		map[char_right] = right;

		// Update the max Length
		maxLength = max(maxLength, right - left + 1);
	}
	return maxLength;
}
// @lc code=end
