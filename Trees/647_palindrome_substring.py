class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        # odd
        for i in range(len(s)):
            start = i
            end = i
            while (start >= 0) and (end < len(s)) and (s[start] == s[end]) :
                start -= 1
                end += 1
            if (end-start+1)%2 == 1:
                cnt += 1
        # even
        for i in range(len(s)):
            start = i
            end = i+1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            if (end-start+1)%2 == 0:
                cnt += 1
        return cnt
        
        
sol = Solution()
s = "abc"
print(sol.countSubstrings(s))