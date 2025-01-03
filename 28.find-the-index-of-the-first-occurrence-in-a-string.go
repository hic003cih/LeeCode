/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Find the Index of the First Occurrence in a String
 */

//haystack = "sadbutsad", needle = "sad"
// Output:0

// @lc code=start
func strStr(haystack string, needle string) int {

	if len(needle) == 0 {
		return 0
	}

	m, n := len(needle), len(haystack)

	for i := 0; i < n-m; i++ {
		if haystack[i:i+m] == needle {
			return i
		}
	}

	return -1

	// if len(needle) == 0 {
	// 	return 0
	// }

	// m, n := len(needle), len(haystack)

	// // Sliding window approach
	// //n-m 為了限制不要超出比較的長度,不要超出needle的長度
	// //haystack = "leetcode", needle = "leeto"
	// // i ~ i+m 每移動一次,就跟著i+m

	// for i := 0; i <= n-m; i++ {
	// 	if haystack[i:i+m] == needle {
	// 		return i
	// 	}
	// }

	// return -1
}

// @lc code=end

