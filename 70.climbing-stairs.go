/*
 * @lc app=leetcode id=70 lang=golang
 *
 * [70] Climbing Stairs
 */

//  You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

// @lc code=start
func climbStairs(n int) int {

	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}

	first, second := 1, 2
	for i := 3; i <= n; i++ {
		current := first + second
		first = second
		second = current
	}
	return second

	// //If it's only 1 and 2, return directly
	// if n == 1 {
	// 	return 1
	// }
	// if n == 2 {
	// 	return 2
	// }

	// dp := make([]int, n+1)
	// //Preset 1-step and 2-step as fixed steps.
	// dp[1] = 1
	// dp[2] = 2

	// //Start from 3, up to n , each level is the sum of the previous two terms.
	// for i := 3; i <= n; i++ {
	// 	dp[i] = dp[i-1] + dp[i-2]
	// }

	// //current = 3
	// /
	// return dp[n]
	// // 	The 5 distinct ways are:

	// // [1, 1, 1, 1]
	// // [1, 1, 2]
	// // [1, 2, 1]
	// // [2, 1, 1]
	// // [2, 2]

}

// @lc code=end

