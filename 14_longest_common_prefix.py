class Solution:
    '''
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
    '''
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        common_st = strs[0]
        if len(strs) > 1:
            for st in strs[1:]:
                min_len = len(common_st) if len(st) > len(common_st) else len(st)
                common_st = common_st[0:min_len]
                common = ""
                for idx in range(len(common_st)):
                    # import pdb
                    # pdb.set_trace()
                    if st[idx] != common_st[idx]:
                        # import pdb
                        # pdb.set_trace()
                        break
                    if idx == 0:
                        common = st[0]
                    else:
                        common = st[0:idx+1]
                common_st = common
        return common_st


sol = Solution()
strs = ["dog","racecar","car"]
# strs = ["ab","a"]
print(sol.longestCommonPrefix(strs))
