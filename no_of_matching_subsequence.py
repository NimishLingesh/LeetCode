class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if self.isSubsequence(word, s):
                count += 1
        return count

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
        # print(pos)
        # print(len(s))
        if len(s) == (pos):
            return True
        else:
            return False
        

s = "abcde"
words = ["a","bb","acd","ace"]
sol = Solution()
print(sol.numMatchingSubseq(s, words))
