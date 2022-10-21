class Solution:
    def countAndSay(self, n: int) -> str:
        return self.helper(n)
    
    def helper(self, num):
        if num == 0:
            return ""
        s = "1"
        ret = ""
        num -= 1
        while(num>0):
            prev = s[0]
            cnt = 1
            for ch in s[1:]:
                if ch == prev:
                    cnt += 1
                elif cnt>1:
                    ret += str(cnt) + prev
                    cnt = 1
                    prev = ch
                else:
                    ret += "1" + prev
                    prev = ch
                    cnt = 1
            if cnt>1:
                ret += str(cnt) + prev
            else:
                ret += "1" + prev
            num -= 1
            s = ret
            ret = ""
            print(s)
        return s