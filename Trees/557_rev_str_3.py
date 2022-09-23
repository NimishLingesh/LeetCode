class Solution:
    def reverseWords(self, s: str) -> str:
        ll = s.split(" ")
        res = ""
        for idx, word in enumerate(ll):
            res += word[::-1] + " "
        return res[:-1]