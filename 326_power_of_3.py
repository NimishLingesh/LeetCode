from re import M


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n >= 3:
            num = n//3
            den = n/3
            if den-num > 0:
                return False
            n = n/3
        if n == 1:
            return True
        else:
            return False

sol = Solution()
n = 45
print(sol.isPowerOfThree(n))