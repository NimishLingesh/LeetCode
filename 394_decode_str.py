class Solution:
    def decodeString(self, s: str):
        while len(s) != 0:
            num = s.pop(0)
            num = int(num)


48-57

sol = Solution()
s = "3[a]2[bc]"
# s = "3[a2[c]]"
print(sol.decodeString(s))