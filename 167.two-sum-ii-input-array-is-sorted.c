/*
 * @lc app=leetcode id=167 lang=c
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
// #include "uthash.h"

typedef struct
{
	int key;
	int value;
	UT_hash_handle hh;
} HashItem;

// 函式來安全地釋放整個雜湊表
void free_hash_map(HashItem **map)
{
	HashItem *current_item, *tmp;
	HASH_ITER(hh, *map, current_item, tmp)
	{
		HASH_DEL(*map, current_item); // 從雜湊表中刪除
		free(current_item);			  // 釋放結構本身的記憶體
	}
}
int *twoSum(int *numbers, int numbersSize, int target, int *returnSize)
{
	// // Brute-Force approach
	// *returnSize = 2; // 回傳的陣列大小固定為 2
	// int *result = (int *)malloc(2 * sizeof(int));

	// if (result == NULL)
	// {
	// 	*returnSize = 0;
	// 	return NULL;
	// }

	// for (int i = 0; i < numbersSize; i++)
	// {
	// 	for (int j = i + 1; j < numbersSize; j++)
	// 	{
	// 		if (numbers[i] + numbers[j] == target)
	// 		{
	// 			result[0] = i + 1;
	// 			result[1] = j + 1;
	// 			return result;
	// 		}
	// 	}
	// }
	// // 根據題目保證，一定會找到解，所以理論上不會執行到這裡
	// *returnSize = 0;
	// free(result);
	// return NULL;

	// // Brute-force approach + Sorting

	// Handle edge case where the array has fewer than two elements.
	// if (numbersSize < 2)
	// {
	// 	*returnSize = 0;
	// 	return NULL;
	// }
	// // Iterate through all possible pairs with a nested loop.
	// for (int i = 0; i < numbersSize; i++)
	// {
	// 	// The inner loop must start from the element after 'i'.
	// 	for (int j = i + 1; j < numbersSize; j++)
	// 	{

	// 		if (numbers[i] + numbers[j] == target)
	// 		{
	// 			*returnSize = 2;
	// 			// Allocate memory for the result
	// 			int *result = (int *)malloc(2 * sizeof(int));
	// 			// Check if memory allocation failed.
	// 			if (result == NULL)
	// 			{
	// 				*returnSize = 0;
	// 				return NULL;
	// 			}
	// 			result[0] = i + 1;
	// 			result[1] = j + 1;
	// 			return result;
	// 		}
	// 		// Optimization : Since the array is sorted, if the current current_sum is already greater than the target.
	// 		// all subsequent numbers for 'j' will also result in a current_sum that is too large.
	// 		// Thus, we can break out of the inner loop early.
	// 		if (numbers[i] + numbers[j] > target)
	// 		{
	// 			break;
	// 		}
	// 	}
	// }
	// // If the loops complete, no solution was found.
	// *returnSize = 0;
	// return NULL;

	// // Two-Pointers approach

	// // Handle edge case where the array has fewer tha two elements.
	// if (numbersSize < 2)
	// {
	// 	*returnSize = 0;
	// 	return NULL;
	// }

	// int left = 0;
	// int right = numbersSize - 1;

	// // Scan the array from both ends using two pointers.
	// while (left < right)
	// {
	// 	int current_sum = numbers[left] + numbers[right];

	// 	if (current_sum == target)
	// 	{
	// 		// Allocate memory for the result.
	// 		int *result = (int *)malloc(2 * sizeof(int));
	// 		// Check if memory allocation failed.
	// 		if (result == NULL)
	// 		{
	// 			*returnSize = 0;
	// 			return NULL;
	// 		}
	// 		*returnSize = 2;
	// 		result[0] = left + 1;
	// 		result[1] = right + 1;
	// 		return result;
	// 	}
	// 	// If the current_sum is smaller than the target, move the left pointer to increase the current_sum.
	// 	else if (current_sum < target)
	// 	{
	// 		left++;
	// 	}
	// 	else
	// 	{
	// 		// If the current_sum is greater than the target, move the right pointer to decrease the current_sum.
	// 		// current_sum > target
	// 		right--;
	// 	}
	// }
	// // If the loops complete, no solution was found.
	// *returnSize = 0;
	// return NULL;

	// Hash Map
	if (numbersSize < 2)
	{
		*returnSize = 0;
		return NULL;
	}

	HashItem *map = NULL; // 初始化雜湊表為 NULL

	for (int i = 0; i < numbersSize; i++)
	{
		int complement = target - numbers[i];
		HashItem *found_item;

		HASH_FIND_INT(map, &complement, found_item);

		if (found_item != NULL)
		{

			// Allocate memory for the result.
			int *result = (int *)malloc(2 * sizeof(int));
			if (result == NULL)
			{
				*returnSize = 0;
				free_hash_map(&map); // 分配失敗也要釋放之前的所有記憶體
				return NULL;
			}
			*returnSize = 2;
			// The stored index is 0-based, so we add 1 for the required 1-based output.
			result[0] = found_item->value + 1;
			result[1] = i + 1;

			// Clean up the hash map before returning, as it's no longer needed.
			free_hash_map(&map);

			return result;
		}
		// If the result is not found, add the current number and index to the hash map
		HashItem *new_item = (HashItem *)malloc(sizeof(HashItem));
		if (new_item == NULL)
		{
			*returnSize = 0;
			free_hash_map(&map);
			return NULL;
		}
		new_item->key = numbers[i];
		new_item->value = i;
		HASH_ADD_INT(map, key, new_item);
	}

	free_hash_map(&map);
	*returnSize = 0;
	return NULL;
}
// @lc code=end
