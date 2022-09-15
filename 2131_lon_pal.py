class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        bucket = []
        same_ch = {}
        cnt = 0
        for i in range(len(words)):
            rev = words[i][::-1]
            if rev in bucket:
                cnt += 4
                words[i] = ""
            else:
                if words[i][0] == words[i][1]:
                    ch = words[i][0]
                    if same_ch.get(ch):
                        same_ch[ch] += 1
                    else:
                        same_ch[ch] = 1
                else:
                    bucket.append(words[i])
        visited = 0
        for key, val in same_ch.items():
            if val%2 == 1:
                if not visited:
                    visited = 1
                    cnt += 2*val
                else:
                    cnt += 2*(val-1)
            else:
                cnt += 2*val
        return cnt


words = ["lc","cl","gg"]
words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
words = ["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]
sol = Solution()
print(sol.longestPalindrome(words))