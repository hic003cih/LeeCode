/*
 * @lc app=leetcode id=5 lang=golang
 *
 * [5] Longest Palindromic Substring
 */

//  Example 1:

// Input: s = "babad"
// Output: "bab"
// Explanation: "aba" is also a valid answer.

// Example 2:

// Input: s = "cbbd"
// Output: "bb"

// @lc code=start
func longestPalindrome(s string) string {
	if len(s) < 2 {
		return s
	}

	start, end := 0, 0

	for i := 0; i < len(s); i++ {
		// Odd-length palindrome
		len1 := expandAroundCenter(s, i, i)
		// Even-length palindrome
		len2 := expandAroundCenter(s, i, i+1)

		// Get the longer palindrome
		maxLen := max(len1, len2)

		// Update start and end indices for the longest palindrome found so far
		if maxLen > end-start {
			//向左延伸 (maxLen-1)/2 的距離。
			//回文的中心點不需要減去（中心點本身就是回文的一部分）。
			start = i - (maxLen-1)/2
			//向右延伸 maxLen/2 的距離。
			end = i + maxLen/2
		}
	}

	return s[start : end+1]
}

func expandAroundCenter(s string, left, right int) int {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	// left + 1 是回文的實際左邊界。
	// right - 1 是回文的實際右邊界。
	// (right - 1) - (left + 1) + 1 = right - left - 1
	return right - left - 1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

