class Solution:
    def isHappy(self, n: int) -> bool:
        s_num = str(n)
        sum = 0
        for ch in s_num:
            sum += (ord(ch)-48)**2
        s_num = str(sum)
        l = [sum]
        while True:
            sum = 0
            for ch in s_num:
                sum += (ord(ch)-48)**2
            if sum == 1:
                return True
            elif sum in l:
                return False
            else:
                l.append(sum)
            s_num = str(sum)
sol = Solution()
n=3
print(sol.isHappy(n))