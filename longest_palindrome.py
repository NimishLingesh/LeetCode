class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        ch_map = {}
        for ch in s:
            if ch not in ch_map.keys():
                ch_map[ch] = 1
            else:
                ch_map[ch] += 1

        odd = False
        for key, val in ch_map.items():
            if val % 2 == 0:
                count += val
            else:
                odd = True
                count += val - 1
        if odd:
            return count + 1
        else:
            return count
            



s = "a"
sol = Solution()
print(sol.longestPalindrome(s))
