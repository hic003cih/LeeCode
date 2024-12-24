/*
 * @lc app=leetcode id=67 lang=golang
 *
 * [67] Add Binary
 */

// @lc code=start
func addBinary(a string, b string) string {
	//     1010
	//     1011
	//   10101

	result := ""
	carry := 0

	i, j := len(a)-1, len(b)-1

	for i >= 0 || j >= 0 || carry > 0 {
		sum := carry

		if i >= 0 {
			sum += int(a[i] - '0')
			i--
		}
		if j >= 0 {
			sum += int(b[j] - '0')
			j--
		}

		result = string(sum%2+'0') + result
		carry = sum / 2
	}

	return result
	// result := ""
	// carry := 0

	// i, j := len(a)-1, len(b)-1

	// // Loop through both strings from right to left
	// for i >= 0 || j >= 0 || carry > 0 {
	// 	sum := carry

	// 	if i >= 0 {
	// 		sum += int(a[i] - '0')
	// 		i--
	// 	}
	// 	if j >= 0 {
	// 		sum += int(b[j] - '0')
	// 		j--
	// 	}

	// 	// Compute the current digit and update the carry
	// 	result = string(sum%2+'0') + result
	// 	carry = sum / 2
	// }

	// return result
}

// @lc code=end

