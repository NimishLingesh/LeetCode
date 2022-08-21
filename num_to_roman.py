class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_roman = {
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
            "0": "",
        }


sol = Solution()
num = 19
print(sol.intToRoman(num))
