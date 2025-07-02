/*
 * @lc app=leetcode id=219 lang=c
 *
 * [219] Contains Duplicate II
 */
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
// #include "uthash.h" // 假設 uthash.h 標頭檔已在環境中

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
// @lc code=start
bool containsNearbyDuplicate(int *nums, int numsSize, int k)
{
	// // Brute - force approach
	// for (int i = 0; i < numsSize; i++)
	// {
	// 	for (int j = i + 1; j < numsSize; j++)
	// 	{
	// 		// If the distance between indices exceeds the k, stop searching for the current element
	// 		if (j - i > k)
	// 		{
	// 			break;
	// 		}
	// 		if (nums[i] == nums[j])
	// 		{
	// 			return true;
	// 		}
	// 	}
	// }
	// return false;

	// // Hash Map

	// if (k <= 0)
	// {
	// 	return false;
	// }

	// HashItem *map = NULL;

	// for (int i = 0; i < numsSize; i++)
	// {
	// 	int current_num = nums[i];
	// 	HashItem *found_item;
	// 	HASH_FIND_INT(map, &current_num, found_item);

	// 	if (found_item != NULL)
	// 	{
	// 		if (i - found_item->value <= k)
	// 		{
	// 			// 清理雜湊表並返回
	// 			free_hash_map(&map);
	// 			return true;
	// 		}
	// 	}
	// 	else
	// 	{
	// 		// If the item does not exist in the map, create it and add it.
	// 		found_item = (HashItem *)malloc(sizeof(HashItem));
	// 		if (found_item == NULL)
	// 		{
	// 			free_hash_map(&map);
	// 			return false;
	// 		}
	// 		found_item->key = current_num;
	// 		HASH_ADD_INT(map, key, found_item);
	// 	}
	// 	// Update this number's newest index
	// 	found_item->value = i;
	// }
	// free_hash_map(&map);
	// return false;

	// Sliding window+Hash set
	if (k <= 0)
	{
		return false;
	}
	// This hash set represents our sliding window.
	HashItem *set = NULL;

	for (int i = 0; i < numsSize; i++)
	{
		int current_num = nums[i];
		HashItem *found_item;

		// 1. Check: Is the current number already in our window?
		HASH_FIND_INT(set, &current_num, found_item);
		if (found_item != NULL)
		{
			// Yes, a duplicate is found within the k-distance window.
			free_hash_set(&set);
			return true;
		}

		// 2. Add: Add the current number to the window.
		HashItem *new_item = malloc(sizeof(HashItem));
		if (new_item == NULL)
		{
			free_hash_set(&set);
			return false; // Memory allocation failure
		}
		new_item->key = current_num;
		HASH_ADD_INT(set, key, new_item);

		// 3. Maintain: If the window size now exceeds k, remove the oldest element.
		// HASH_COUNT can be slow, a simple counter is faster, but for clarity:
		if (HASH_COUNT(set) > k)
		{
			int oldest_num = nums[i - k];
			HashItem *item_to_delete;
			HASH_FIND_INT(set, &oldest_num, item_to_delete);
			if (item_to_delete != NULL)
			{
				HASH_DEL(set, item_to_delete);
				free(item_to_delete);
			}
		}
	}
}
// @lc code=end
