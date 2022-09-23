class Solution:
    def findLength(self, nums1, nums2) -> int:
        # Using DP, constructing a 2D matrix for the dp variable 

        A = nums1
        B = nums2
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)


        # TLE
        """
        max_count = 0
        l_n1 = len(nums1)
        l_n2 = len(nums2)
        for idx_f, first in enumerate(nums1):
            for idx_s, second in enumerate(nums2):
                count = 0
                if first == second:
                    # count += 1
                    i = idx_f
                    j = idx_s
                    while i<l_n1 and j<l_n2 and nums1[i] == nums2[j]:
                        count += 1
                        i += 1
                        j += 1
                    # count += 1
                    # nums2[idx] = "#"
                    # break
                if count > max_count:
                    max_count = count
        return max_count
        """

n1 = [0,0,0,0,1]
n2 = [1,0,0,0,0]
sol = Solution()
print(sol.findLength(n1, n2))