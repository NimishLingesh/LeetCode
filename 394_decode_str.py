class Solution:
    def decodeString(self, s: str):
        while len(s) != 0:
            num = s.pop(0)
            num = int(num)
            

sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))