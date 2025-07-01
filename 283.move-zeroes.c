/*
 * @lc app=leetcode id=283 lang=c
 *
 * [283] Move Zeroes
 */
#include <stdio.h>

// void swap(int *a, int *b)
// {
// 	int temp = *a;
// 	*a = *b;
// 	*b = temp;
// }

// @lc code=start
void moveZeroes(int *nums, int numsSize)
{
	// // Brute-force approach
	// for (int i = 0; i < numsSize; i++)
	// {
	// 	if (nums[i] == 0)
	// 	{
	// 		// Iterate through the remaining numbers
	// 		// To swap with the first non-zero number found
	// 		for (int j = i + 1; j < numsSize; j++)
	// 		{
	// 			if (nums[j] != 0)
	// 			{

	// 				// swap(&nums[i], &nums[j]);
	// 				int temp = nums[i];
	// 				nums[i] = nums[j];
	// 				nums[j] = temp;
	// 				break;
	// 			}
	// 		}
	// 	}
	// }

	// // Two-Pointers
	// // This is not the optimal two-pointers approach with O(n) time complexity and O(1) space complexity
	// // Handle null or empty array case.
	// if (nums == NULL || numsSize == 0)
	// {
	// 	return;
	// }
	// //'slow' pointers marks the position where the next non-zero element should be placed.
	// int slow = 0;

	// // First pass: Move all non-zero elements to the front of the array.
	// for (int fast = 0; fast < numsSize; fast++)
	// {
	// 	if (nums[fast] != 0)
	// 	{
	// 		nums[slow] = nums[fast];
	// 		slow++;
	// 	}
	// }
	// // Second pass:After all non-zero elements are moved, fill the rest of the array with zeros.
	// for (int i = slow; i < numsSize; i++)
	// {
	// 	nums[i] = 0;
	// }

	// Two-Pointers
	//  This is the optimal two-pointers approach
	if (nums == NULL || numsSize == 0)
	{
		return;
	}

	for (int slow = 0, fast = 0; fast < numsSize; fast++)
	{
		// If a non-zero element is found by the fast pointer, move it to the slow pointer's position
		if (nums[fast] != 0)
		{
			// To avoid self-swapping, only perform the swap if the pointers are not at the same position.
			if (slow != fast)
			{
				int temp = nums[slow];
				nums[slow] = nums[fast];
				nums[fast] = temp;
			}
			// The slow pointer always advance after a non-zero element has been placed.
			slow++;
		}
	}
}
// @lc code=end
