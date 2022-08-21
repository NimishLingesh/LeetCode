class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = 0
        var = 0
        cis = 0
        cas = 0
        for ch in s:
            try:
                # import pdb

                # pdb.set_trace()
                if ch == "-" and var == 0:
                    var = -1
                    continue
                elif ch == "+" and var == 0:
                    var = 1
                    continue
                if ch == " " and cis == 0:
                    continue
                cis = 1
                tmp = int(ch)
                cas = 1
                num = num * 10 + tmp
            except Exception:
                if cis:
                    if var == -1:
                        num = -num
                    if num < -pow(2, 31):
                        return -pow(2, 31)
                    elif num > pow(2, 31) - 1:
                        return pow(2, 31) - 1
                    else:
                        return num
                return 0
        if var == -1:
            num = -num
        if num < -pow(2, 31):
            return -pow(2, 31)
        elif num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return num


sol = Solution()
num = sol.myAtoi("+1")
print(num)
