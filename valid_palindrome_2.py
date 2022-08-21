from audioop import reverse


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1 : right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

    #     s1 = list(s[0 : len(s) // 2])
    #     s2 = list(s[(len(s) // 2) :][::-1])
    #     # s2 = s2[::-1]
    #     print(s1)
    #     print(s2)
    #     # tmp = 0
    #     str_len = len(s2)
    #     valid = 1
    #     for i in range(0, str_len):
    #         if s1[i] != s2[i]:
    #             # tmp = 1
    #             # i -= 1
    #             # str_len += 1
    #             if s1[i] == s2[i + 1]:
    #                 # s2.pop(i)
    #                 valid = self.check_validity(s1[i:], s2[i + 1 :])
    #                 if valid:
    #                     return valid
    #             elif s2[i] == s1[i + 1]:
    #                 lhs = s1[i + 1 :]
    #                 lhs.append(s2[-1])
    #                 valid = self.check_validity(lhs, s2[i:-1])
    #                 return valid
    #                 # s1.pop(i)
    #             else:
    #                 valid = 0
    #     return valid

    # def check_validity(self, s1, s2):
    #     print("---")
    #     print(s1)
    #     print(s2)
    #     valid = 1
    #     for inx, val in enumerate(s1):
    #         if val != s2[inx]:
    #             valid = 0
    #     return valid

    # tmp = 1
    # j = 0
    # k = 1
    # valid = 1
    # for i in range(0, len(s) // 2):
    #     lhs = i + j
    #     rhs = i + k
    #     if s[lhs] != s[-(rhs)] and tmp:
    #         tmp = 0
    #         # import pdb

    #         # pdb.set_trace()

    #         if s[lhs] == s[-(rhs + 1)]:
    #             # s.pop(-(i + 1))
    #             k = 2
    #             # s = s[0 : -(i + 1)] + s[-i:]
    #         elif s[lhs + 1] == s[-(rhs)]:
    #             j = 1
    #             # s.pop(i)
    #             # s = s[0:i] + s[i + 1 :]
    #         else:
    #             valid = 0
    #     elif s[lhs] != s[-(rhs)]:
    #         valid = 0
    # print(s)
    # return valid


sol = Solution()
s = "aba"

res = sol.validPalindrome(s)
print(res)
