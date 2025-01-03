/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */
//  Input: s = "abcabcbb"
//  Output: 3
//  Explanation: The answer is "abc", with the length of 3.
//  Example 2:

//  Input: s = "bbbbb"
//  Output: 1
//  Explanation: The answer is "b", with the length of 1.
//  Example 3:

//  Input: s = "pwwkew"
//  Output: 3
//  Explanation: The answer is "wke", with the length of 3.
//  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	charMap := make(map[byte]int)
	maxLength := 0
	start := 0

	//第一個指針循環
	for end := 0; end < len(s); end++ {
		// Check if s[end] is already in the map and within the current window.
		if idx, exists := charMap[s[end]]; exists && idx >= start {
			//第二個指針往前
			start = idx + 1 // Move start to the right of the duplicate
		}
		charMap[s[end]] = end                   // Update the last index of the current character
		maxLength = max(maxLength, end-start+1) // Calculate the length of the current substring and update maxLength if necessary.
	}

	return maxLength
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

