class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        
        diff = 10 - k
        res = []
        for i in diff:
            first_digit = i+1
            if first_digit == 0:
                continue
            idx_cnt = 1
            num = i + ""
            odd = str(i)
            even = str(i+n)
            while idx_cnt != n+1:
                if idx_cnt % 2 == 1:
                    num += odd
                else:
                    num += even 
            res.append(num)
        print(res)

sol = Solution()
n = 3
k = 7
print(sol.numsSameConsecDiff(3, 7))