/*
 * @lc app=leetcode id=58 lang=golang
 *
 * [58] Length of Last Word
 */

// @lc code=start
func lengthOfLastWord(s string) int {
	// Trim trailing spaces to handle cases like "Hello World   "
	s = strings.TrimSpace(s)

	// Split the string by spaces
	words := strings.Split(s, " ")

	// Return the length of the last word
	return len(words[len(words)-1])

	// Example Input/Output:
	// words = ["Hello", "World"]
	// Last word: "World"
	// Length: 5
}

// @lc code=end

