/*
 * @lc app=leetcode id=118 lang=golang
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
func generate(numRows int) [][]int {

	triangle := make([][]int, numRows)

	//橫的numRows(排)
	for i := 0; i < numRows; i++ {
		//初始化第 i 行為一個長度為 i+1 的切片（每行的元素數等於行數 i+1）
		row := make([]int, i+1)
		//每個的首尾都一定是1,直接首尾都設成1
		row[0], row[len(row)-1] = 1, 1

		// 當i=0和1時,都沒中間元素,所以大於1時才要填充中間元素
		// j是直排的位置,小於i是因為每個橫排中間元素都會有i-1個
		for j := 1; j < i; j++ {
			//triangle[i-1][j-1] 是上一行的左側數字
			//triangle[i-1][j] 是上一行的右側數字
			row[j] = triangle[i-1][j-1] + triangle[i-1][j] // 計算上一行相鄰兩數之和
		}

		// 將生成的第 i 行添加到 Pascal's Triangle
		triangle[i] = row
	}

	return triangle
}

// @lc code=end

