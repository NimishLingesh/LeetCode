class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        offset = 1
        total = 0
        
        for digit1 in num1[::-1]:
            curr_total, curr, carry = 0, offset, 0
            for digit2 in num2[::-1]:
                new = int(digit1) * int(digit2) + carry
                carry, new = new // 10, new % 10
                curr_total += new * curr
                curr *= 10
            curr_total += curr * carry
            total += curr_total
            offset *= 10
        
        return str(total)