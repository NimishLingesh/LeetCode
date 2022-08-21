class Solution:
    def letterCombinations(self, digits: str):
        from itertools import permutations

        num_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        l = []
        str_len = len(digits)
        for ch in digits:
            

sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))
