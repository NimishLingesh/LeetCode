class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x > 0:
            num = x
        else:
            num = -x

        while num != 0:
            rev = rev * 10 + num % 10
            num = int(num / 10)

        if rev < -pow(2, 31) or rev > pow(2, 31) - 1:
            return 0
        else:
            if x > 0:
                return rev
            else:
                return -rev


sol = Solution()
res = sol.reverse(321)
print(res)
