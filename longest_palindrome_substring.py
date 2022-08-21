class Solution:
    def __init__(self):
        self.list_indices = []
        self.max_num = 0
        self.max_val = ""
        self.given_string = ""

    def longestPalindrome(self, s):
        self.given_string = s
        if len(s) > 2:
            if len(s) % 2 == 1:
                self.findIndices_odd(s)
                self.findPalindrome_odd(s)
            else:
                self.findIndices(s)
                self.findPalindrome(s)
            print(self.list_indices)
            return self.max_val
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        elif len(s) == 1:
            return s
        else:
            return ""

    def findIndices_odd(self, s):
        for ind in range(1, len(s) - 1):
            if s[ind - 1] == s[ind + 1]:
                self.list_indices.append(ind)
            if s[ind - 1] == s[ind]:
                self.assignMax(2, s[ind] + s[ind])
            if s[ind] == s[ind + 1]:
                self.assignMax(2, s[ind] + s[ind])

    def findPalindrome_odd(self, s):
        if len(self.list_indices) == 0:
            self.assignMax(1, s[0])
            return
        for ind in self.list_indices:
            i = ind - 1
            j = ind + 1
            count = 0
            str_val = s[ind]
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    str_val = s[i] + str_val + s[j]
                    i -= 1
                    j += 1
                    count += 1
                    continue
                else:
                    break
            self.assignMax(count * 2 + 1, str_val)

    def findIndices(self, s):
        for ind in range(1, len(s) - 1):
            if s[ind - 1] == s[ind + 1]:
                self.list_indices.append(ind)
            if s[ind - 1] == s[ind]:
                self.assignMax(2, s[ind] + s[ind])
            if s[ind] == s[ind + 1]:
                self.assignMax(2, s[ind] + s[ind])

    def findPalindrome(self, s):
        if len(self.list_indices) == 0:
            self.assignMax(1, s[0])
            return
        for ind in self.list_indices:
            i = ind - 1
            j = ind + 1
            count = 0
            str_val = s[ind]
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    str_val = s[i] + str_val + s[j]
                    i -= 1
                    j += 1
                    count += 1
                    continue
                else:
                    break
            self.assignMax(count * 2 + 1, str_val)

    def assignMax(self, num, str_val):
        if num > self.max_num:
            self.max_num = num
            self.max_val = str_val


if __name__ == "__main__":
    sol = Solution()
    stri = "aaaa"
    resp = sol.longestPalindrome(stri)
    print(resp)
