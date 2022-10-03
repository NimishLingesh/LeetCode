class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        dp[m-1][n-1] = 1
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if dp[r][c] == 0:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]