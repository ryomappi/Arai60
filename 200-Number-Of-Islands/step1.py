class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int):
        if not (0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1):
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"  # Mark as visited
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
