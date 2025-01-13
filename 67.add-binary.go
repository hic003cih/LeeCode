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

	i, j := len(a)-1, len(b)-1 // 從末尾開始

	//
	for i >= 0 || j >= 0 || carry > 0 { // 當 a, b 還有數字或者有進位時
		sum := carry // 初始化當前位的總和為進位值

		if i >= 0 {
			sum += int(a[i] - '0') // 將 a 的當前位轉換為數字並加到 sum
			i--
		}
		if j >= 0 {
			sum += int(b[j] - '0') // 將 b 的當前位轉換為數字並加到 sum
			// '0' - '0' = 48 - 48 = 0
			// '1' - '0' = 49 - 48 = 1
			j--
		}

		result = string(sum%2+'0') + result // 當前位的結果加入最前面
		carry = sum / 2                     // 計算進位
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

