/*
 * @lc app=leetcode id=344 lang=c
 *
 * [344] Reverse String
 */
#include <stdio.h>

// @lc code=start
void reverseHelper(char *s, int left, int right)
{
	// Base case : If the pointers meet or cross, the recursion stops.
	if (left >= right)
	{
		return;
	}
	// 1. Swap the characters at the current left and right boundaries.
	char temp = s[left];
	s[left] = s[right];
	s[right] = temp;
	// 2. Recursively call the function for the inner substring.
	reverseHelper(s, left + 1, right - 1);
}
void reverseString(char *s, int sSize)
{
	// // Recursion approach
	// if (s == NULL || sSize <= 1)
	// {
	// 	return;
	// }
	// reverseHelper(s, 0, sSize - 1);

	// Two-Pointer
	if (s == NULL || sSize <= 1)
	{
		return;
	}
	int left = 0;
	int right = sSize - 1;
	while (left < right)
	{
		char temp = s[left];
		s[left] = s[right];
		s[right] = temp;
		left++;
		right--;
	}
}
// @lc code=end
