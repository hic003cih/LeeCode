/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

//  nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
//  Execution:
//  i = 1: Compare nums[1] with nums[0] → Duplicate.
//  i = 2: Compare nums[2] with nums[0] → Unique, update nums[1] = 1.
//  Repeat for all elements.
//  Result:
//  nums = [0, 1, 2, 3, 4, _, _, _, _, _] // First five elements are unique
//  Return: 5

// @lc code=start
func removeDuplicates(nums []int) int {

	//因為要求不能用額外的空間,所以用雙指針來解決
	if len(nums) == 0 {
		return 0
	}

	j := 0

	for i := 1; i < len(nums); i++ {

		if nums[i] != nums[j] {
			//當不是重複時,j移動至下一個點存入不重複的值
			j++
			nums[j] = nums[i]
		}
	}
	//總共有幾個不同的值
	return j + 1

	// if len(nums) == 0 {
	// 	return 0
	// }

	// j := 0
	// for i := 1; i < len(nums); i++ {
	// 	if nums[i] != nums[j] {
	// 		j++
	// 		nums[j] = nums[i]
	// 	}
	// }

	// return j + 1
}

// @lc code=end

