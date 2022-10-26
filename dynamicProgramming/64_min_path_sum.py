class Solution:
    def minPathSum(self, grid) -> int:
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if row_idx == 0 and col_idx == 0:
                    continue
                if row_idx == 0:
                    grid[row_idx][col_idx] += grid[row_idx][col_idx-1]
                elif col_idx == 0:
                    grid[row_idx][col_idx] += grid[row_idx-1][col_idx]
                else:
                    grid[row_idx][col_idx] += min(grid[row_idx-1][col_idx], grid[row_idx][col_idx-1])
        return grid[-1][-1]
