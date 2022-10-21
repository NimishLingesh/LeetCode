from curses.ascii import isalpha
from re import S


class Solution:
    def compress(self, s):
        if len(s)==1:
            return s
        ret = ""
        prev = s[0]
        cnt = 1
        for ch in s[1:]:
            if ch == prev:
                cnt += 1
            elif cnt>1:
                ret += prev + "," + str(cnt)
                cnt = 1
                prev = ch
            else:
                ret += prev
                prev = ch
                cnt = 1
        if cnt>1:
            ret += prev + str(cnt)
        else:
            ret += prev
        return ret


    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        compressed_s = self.compress(s)
        tmp = None
        tmp_no = ""

        cnt_dict = {}
        for ch in compressed_s.spli(","):
            if len(ch) == 1:

            else:
                c = ch[0]
                count = int(ch[1:])
        compressed_s

sol = Solution()
s = "aaabcccd"
# s = "aaaaaaaaaaa"
k = 2
print(sol.getLengthOfOptimalCompression(s, k))