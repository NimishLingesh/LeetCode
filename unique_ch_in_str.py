class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        for idx, ch in enumerate(s):
            if ch not in s[idx+1:] and ch not in lst:
                return idx
            else:
                lst.append(ch)
        return -1

sol = Solution()
s = "aabb"
print(sol.firstUniqChar(s))