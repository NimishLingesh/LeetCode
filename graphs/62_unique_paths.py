class Solution:
    # RECURSIVE SOLUTION
    # def __init__(self) -> None:
    #     self.total_cnt = 0
        
    # def uniquePaths(self, m: int, n: int) -> int:
    #     self.recurse(m-1,n-1)
    #     return self.total_cnt
        
    # def recurse(self, m ,n):
    #     # print(m,n)
    #     if m == 0 and n == 0:
    #         self.total_cnt += 1
    #     if m < 0 or n < 0:
    #         return
    #     self.recurse(m-1, n)
    #     self.recurse(m, n-1)

#####################
# DP solution - works
# start from the enf point =, decrement and reach the start point.
# increment the count as and when it reaches the start point
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        dp[m-1][n-1] = 1
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if dp[r][c] == 0:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]

#######################
# MEMOIZIATION - not yet working 
    def __init__(self) -> None:
        self.total_cnt = 0
        # self.memo = 0
        
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n] * m
        return self.recurse(m-1,n-1, memo)
        
    def recurse(self, row ,col, memo):
        print(memo)
        print("--------")
        if row == 0 and col == 0:
            return 1
        if memo[row][col] != -1:
            return memo[row][col]
        # if row < 0 or col < 0:
        #     return 0
        move_left = 0
        move_up = 0
        if (col>=1):
            move_left = self.recurse(row, col-1, memo)
        if (row>=1):
            move_up = self.recurse(row-1, col, memo)
        memo[row][col] = move_left + move_up
        return memo[row][col] 

sol = Solution()
m = 3
n = 7
print(sol.uniquePaths(m,n))