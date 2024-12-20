package main

/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {
	stack := []rune{}

	bracketMap := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}
	for _, char := range s {
		if openBracket, exits := bracketMap[char]; exits {
			if len(stack) == 0 || stack[len(stack)-1] != openBracket {
				return false
			}
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, char)
		}
	}
	return len(stack) == 0

}

// @lc code=end
