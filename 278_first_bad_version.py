versions = {
    1: True,
    2: True,
    3: True,
    4: False,
    5: False
}

def isBadVersion(version):
    return versions[version]

class Solution(object):
    def __init__(self) -> None:
        self.result = None

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mid = n//2
        left = 1
        right = n
        self.recurse(left, right)
        return self.result

    def recurse(self, left, right):
        mid = (left+right)//2
        if not isBadVersion(mid):
            if isBadVersion(mid-1):
                # first bad version occuring
                self.result = mid
                return mid
            else:
                right = mid
        else:
            # mid = (mid + right)//2
            left = mid
        self.recurse(left, right)
        

sol = Solution()
print(sol.firstBadVersion(5))