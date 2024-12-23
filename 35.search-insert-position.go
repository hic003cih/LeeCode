/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
*/

// @lc code=start
func searchInsert(nums []int, target int) int {

	//用二分法
	left, right := 0, len(nums)-1

	for left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			return mid
			//目標比較大,往右邊找
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return left

	// left, right := 0, len(nums)-1

	// for left <= right {
	//     mid := left + (right-left)/2 // 防止整數溢出

	//     if nums[mid] == target {
	// 	return mid // 找到目標，返回索引
	//     } else if nums[mid] < target {
	// 	left = mid + 1 // 縮小範圍到右半部分
	//     } else {
	// 	right = mid - 1 // 縮小範圍到左半部分
	//     }
	// }

	// return left // 當 left 超過 right 時，left 是插入位置
}

// @lc code=end

