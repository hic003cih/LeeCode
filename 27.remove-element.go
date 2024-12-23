/*
 * @lc app=leetcode id=27 lang=golang
 *
 * [27] Remove Element
 */

// @lc code=start
func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}

	//j是會移動的
	j := 0

	//固定i來循環
	for i := 0; i < len(nums); i++ {
		if nums[i] != val {
			//因為要回傳刪除完以後的nums,所以要先覆蓋,指針再跳下一個
			nums[j] = nums[i]
			j++
		}
	}

	// j := 0 // Pointer for non-val elements

	// for i := 0; i < len(nums); i++ {
	// 	if nums[i] != val {
	// 		nums[j] = nums[i]
	// 		j++ // Move pointer for the next non-val position
	// 	}
	// }

	return j // Number of elements not equal to val
}

// Input: nums = [3, 2, 2, 3], val = 3
// Steps:
// i = 0: nums[0] == 3, skip.
// i = 1: nums[1] != 3, nums[0] = nums[1], increment j = 1.
// i = 2: nums[2] != 3, nums[1] = nums[2], increment j = 2.
// i = 3: nums[3] == 3, skip.
// Result:
// nums = [2, 2, _, _]
// k = 2.

// @lc code=end

