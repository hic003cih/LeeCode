/*
 * @lc app=leetcode id=66 lang=golang
 *
 * [66] Plus One
 */

// @lc code=start
func plusOne(digits []int) []int {

	// 	Input: digits = [1,2,3]
	// Output: [1,2,4]
	// Explanation: The array represents the integer 123.
	// Incrementing by one gives 123 + 1 = 124.
	// Thus, the result should be [1,2,4].

	n := len(digits)

	for i := n - 1; i >= 0; i-- {
		//add 1
		digits[i] += 1

		//The digit is less than 10 means the process ends immediately.
		if digits[i] < 10 {
			//digits[i]++
			return digits
		}
		//If digit is 10, traverse the digits array and set this digit to 0
		digits[i] = 0
	}
	return append([]int{1}, digits...)

	// n := len(digits)

	// // Traverse the array from the last digit
	// for i := n - 1; i >= 0; i-- {
	//     digits[i] += 1
	//     if digits[i] < 10 {
	// 	return digits // No carry, return result
	//     }
	//     digits[i] = 0 // Carry over, set current digit to 0
	// }

	// // If the loop completes, it means all digits were 9
	// return append([]int{1}, digits...)
}

// @lc code=end

