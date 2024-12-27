package main

/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {

	//strs := []string{"flower", "flow", "flight"}
	//len(prefix) = 6, len(str) = 4.
	// The loop reduces prefix:
	// "flower" → "flowe" → "flow".
	// Now, prefix = "flow" matches "flow".

	// Compare with "flight":

	// len(prefix) = 4, len(str) = 6.
	// The loop reduces prefix:
	// "flow" → "flo" → "fl".
	// Now, prefix = "fl" matches "flight[:2].
	// Result:

	// After iterating through all strings, prefix = "fl".

	if len(strs) == 0 {
		return ""
	}

	//{"flower", "flow", "flight"}
	//

	prefix := strs[0] //flower

	//
	for _, str := range strs[1:] {
		for len(prefix) > 0 && (len(prefix) > len(str) || str[:len(prefix)] != prefix) {
			prefix = prefix[:len(prefix)-1]
		}
		if len(prefix) == 0 {
			return ""
		}
	}
	return prefix
}

// @lc code=end
