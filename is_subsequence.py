from re import T


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = 0
        for ch in t:
            if pos < len(s):
                if s[pos] == ch:
                    pos += 1
        print(pos)
        print(len(s))
        if len(s) == (pos):
            return True
        else:
            return False
        # for ch in t:
        #     if len(s) == 0:
        #         return True
        #     if ch == s[0]:
        #         s = s[1:]
        #         print(s)
        # if len(s) == 0 and len(t) == 0:
        #     return True
        # return False

sol = Solution()
s = ""
t = "ahbgdc"
resp = sol.isSubsequence(s, t)
print(resp)
