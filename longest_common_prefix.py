class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs.pop()
        for s in strs:
            prefix = self.compare(prefix, s)
        return prefix

    def compare(self, prefix, s):
        common = ""
        ch_index = 0
        if len(prefix) < len(s):
            for ch in prefix:
                if ch == s[ch_index]:
                    common += ch
                    ch_index += 1
                else:
                    break
        else:
            for ch in s:
                if ch == prefix[ch_index]:
                    common += ch
                    ch_index += 1
                else:
                    break
        return common


sol = Solution()
strs = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(strs))
