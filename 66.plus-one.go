/*
 * @lc app=leetcode id=66 lang=golang
 *
 * [66] Plus One
 */

// @lc code=start
func plusOne(digits []int) []int {

	n := len(digits)

	for i := n - 1; i >= 0; i-- {
		digits[i] = digits[i] + 1

		if digits[i] < 10 {
			return digits
		}
		digits[i] = 0
	}
	return append([]int{1}, digits...)
}

// @lc code=end

// n := len(digits)

// 	for i := n - 1; i >= 0; i-- {
// 		//add 1
// 		digits[i] += 1

// 		//The digit is less than 10 means the process ends immediately.
// 		if digits[i] < 10 {
// 			//digits[i]++
// 			return digits
// 		}
// 		//If digit is 10, traverse the digits array and set this digit to 0
// 		digits[i] = 0
// 	}
// 	return append([]int{1}, digits...)

