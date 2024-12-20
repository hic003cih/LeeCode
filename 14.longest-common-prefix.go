package main

/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	prefix := strs[0]

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
