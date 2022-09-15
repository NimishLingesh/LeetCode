class Solution:
    def __init__(self):
        self.memo = {}
        
    def tribonacci(self, n: int) -> int:
        # Memorization
        if n <= 1:
            return n
        elif n == 2:
            return 1
        if n-1 not in self.memo:
            self.memo[n-1] = self.tribonacci(n-1)
        if n-2 not in self.memo:
            self.memo[n-2] = self.tribonacci(n-2)
        if n-3 not in self.memo:
            self.memo[n-3] = self.tribonacci(n-3)
        return self.memo[n-3] + self.memo[n-1] + self.memo[n-2]

''' Another approach
 def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in xrange(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]
'''
        