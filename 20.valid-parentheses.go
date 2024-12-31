package main

/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

//  Input: "({[]})"
// Initialize:

// stack = []
// Process each character:

// '(': Add to stack → stack = ['('].
// '{': Add to stack → stack = ['(', '{'].
// '[': Add to stack → stack = ['(', '{', '['].
// ']': Matches '[' → Pop → stack = ['(', '{'].
// '}': Matches '{' → Pop → stack = ['('].
// ')': Matches '(' → Pop → stack = [].
// Final Check:

// stack is empty → Return true.
// @lc code=start
func isValid(s string) bool {
	stack := []rune{}

	bracketMap := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	for _, char := range s {
		//查詢char是否在bracketMap中
		//openBracket ->如果是傳入),回傳(
		if openBracket, exits := bracketMap[char]; exits {
			// 如果堆疊為空或者頂部元素不等於對應的開括號
			if len(stack) == 0 || stack[len(stack)-1] != openBracket {
				return false
			}
			//如果最頂部存在對應的key,把char存入stack
			stack = stack[:len(stack)-1]
		} else {
			//如果不存在,把char存入stack
			stack = append(stack, char)
		}
	}
	return len(stack) == 0

	// for _, char := range s {
	// 	if openBracket, exits := bracketMap[char]; exits {
	// 		if len(stack) == 0 || stack[len(stack)-1] != openBracket {
	// 			return false
	// 		}
	// 		stack = stack[:len(stack)-1]
	// 	} else {
	// 		stack = append(stack, char)
	// 	}
	// }
	// return len(stack) == 0

}

// @lc code=end
