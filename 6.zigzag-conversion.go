/*
 * @lc app=leetcode id=6 lang=golang
 *
 * [6] Zigzag Conversion

 Input: s = "PAYPALISHIRING", numRows = 3
*/

// @lc code=start
func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	// Create a slice to hold strings for each row
	rows := make([]string, min())
	curRow := 0
	goingDown := false

	// Traverse the input string
	for _, char := range s {
		rows[curRow] += string(char)
		if curRow == 0 || curRow == numRows-1 {
			goingDown = !goingDown
		}
		if goingDown {
			curRow++
		} else {
			curRow--
		}
	}
	// Combine all rows
	result := ""
	for _, row := range rows {
		result += row
	}
	return result

}

// Utility function to get the minimum of two numbers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

