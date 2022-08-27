class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazine = magazine.split("")
        for ch in ransomNote:
            idx = self.check_idx(ch, magazine)
            print(idx)
            if idx == "not_found":
                return False
            else:
                magazine = magazine[:idx] + magazine[idx+1:]
        return True

    def check_idx(self, ch, magazine):
        for idx, i in enumerate(magazine):
            print(i, idx)
            if ch == i:
                return idx
        return "not_found"

ransomNote = ""
magazine = ""
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))