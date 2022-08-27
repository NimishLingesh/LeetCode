from re import X
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len = len(p)
        if p_len == 1:
            s_enum = s
        else:
            s_enum = s[:-(p_len-1)]
        cnt = list()
        for idx, i in enumerate(s_enum):
            if i in p:
                tmp_str = s[idx:idx+len(p)]
                if sorted(tmp_str) == sorted(p):
                    cnt.append(idx)
        return cnt

sol = Solution()
s = "cbaebabacc"
p = "acb"
print(sol.findAnagrams(s,p))