class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(y, x):
            if 0<=y<m and 0<=x<n and grid[y][x] == "1":
                grid[y][x] = "0"

                dfs(y-1, x)
                dfs(y+1, x)
                dfs(y, x-1)
                dfs(y, x+1)

        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result