class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # for row in range(0, numRows):

        #     for ch in s:
        conv = ""
        cnt = 0
        pos = 0
        place = 0
        while cnt < len(numRows):
            if pos > len(s):
                cnt += 1
                # pos = pos%numRows - numRows
                pos = cnt
            conv += s[pos]
            if place == 0:
                pos = 
            pos += 2 * numRows - 2
        return conv


str1 = "PAYPALISHIRING"
num_rows = 4
sol = Solution()
ret = sol.convert(str1, num_rows)
print(ret)
