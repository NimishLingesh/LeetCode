class Solution:
    def numIslands(self, grid):
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col]!="1":
                return
            # to mark as visited
            # print(row, col)
            grid[row][col] = "#"
            dfs(grid, row-1, col)
            dfs(grid, row, col-1)
            dfs(grid, row+1, col)
            dfs(grid, row, col+1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(grid, row, col)
        return count

sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))