package main

import (
	"strconv"
)

/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
//
//	func cleanString(text string) string {
//		clean_text := strings.ToLower(text)
//		clean_text = strings.Join(strings.Fields(clean_text), "")
//		regexp, _ := regexp.Compile(`[^\p{L}\p{N} ]+`)
//		return regexp.ReplaceAllString(clean_text, "")
//	}
func isPalindrome(x int) bool {
	//clean_text := cleanString(string(x))
	var j int

	text := strconv.Itoa(x)

	for i := 0; i < len(text)/2; i++ {
		//fmt.Println("I:" + strconv.Itoa(i))
		j = len(text) - 1 - i
		//fmt.Println("J:" + strconv.Itoa(j))
		if string(text[i]) != string(text[j]) {
			return false
		}
	}
	return true
}

// func main() {
// 	//fmt.Println(isPalindrome(121)) // true
// 	//fmt.Println(isPalindrome(-121)) // false
// 	// fmt.Println(isPalindrome(10))   // false
// 	fmt.Println(isPalindrome(111111154)) // false
// }

// @lc code=end
