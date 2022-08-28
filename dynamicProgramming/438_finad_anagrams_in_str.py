from re import X
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str):
        # p_len = len(p)
        # if p_len == 1:
        #     s_enum = s
        # else:
        #     s_enum = s[:-(p_len-1)]
        # cnt = list()
        # for idx, i in enumerate(s_enum):
        #     if i in p:
        #         tmp_str = s[idx:idx+len(p)]
        #         if sorted(tmp_str) == sorted(p):
        #             cnt.append(idx)
        # return cnt
        cnt = 0
        if len(p) > len(s):
            return []
        sCount, pCount = {}, {}
        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
        if s[0] == p[0]:
            cnt += 1

        # l to keep track of the index
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            # just remove the empty count key, val hashmap which is idle
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                cnt += 1
        return cnt

sol = Solution()
s = "cbaebabacc"
p = "acb"
print(sol.findAnagrams(s,p))