#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0

        # DFS（深度優先）
        # DFS (Depth-First-Search)
        def dfs(r, c):
            # 超出邊界或已訪問過(變成0)或是是水,直接返回
            # exceed the boundary or visited(transformed to 0) or water, return directly
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            # 將當前位置標記為已訪問
            # mark the current position as visited
            grid[r][c] = '0'
            # 遞歸訪問上下左右四個方向
            # Recursive visit the four directions
            # 向上搜尋
            # Search upward
            dfs(r-1, c)
            # 向下搜尋
            # Search downward
            dfs(r+1, c)
            # 向右搜尋
            # Search to the right
            dfs(r, c+1)
            # 向左搜尋
            # Search to the left
            dfs(r, c-1)
        
        # 遍歷整個網格
        # Traverse the entire grid
        # 先從橫的row再直的column
        # Traverse from row to column
        for r in range(m):
            for c in range(n):
                # 如果當前位置是島嶼，則進行DFS
                # If the current position is an island, perform DFS
                if grid[r][c] == "1":
                    dfs(r, c)
                    # 不管島嶼有沒有連接，都要加1
                    # Add 1 regardless of whether the island is connected or not
                    count += 1
        
        return count


# @lc code=end

