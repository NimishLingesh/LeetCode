class Solution:
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '']
    def intToRoman(self, num: int) -> str:
        result, radix = [], 0
        while num:
            digit, num = num % 10, num // 10
            if digit % 5 == 4:
                result.append(self.symbols[radix] + self.symbols[radix + 1 + (digit // 5)])
            else:
                result.append(self.symbols[radix + 1] * (digit // 5) + self.symbols[radix] * (digit % 5))
            radix += 2
        return ''.join(reversed(result))