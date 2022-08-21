class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            ans += dp[i]
        return ans

    # my solution
    # def numberOfArithmeticSlices(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         cnt = 0
    #         sum = 0
    #         if len(nums) < 3:
    #             return 0
    #         for i, num in enumerate(nums):
    #             print(i, num)
    #             if i == 0:
    #                 continue
    #             diff = num - nums[i - 1]
    #             if i == 1:
    #                 streak = diff

    #             if diff == streak:
    #                 cnt += 1
    #             elif diff != streak:
    #                 streak = diff
    #                 if cnt >= 2:
    #                     sum += self.n_count(cnt - 1)
    #                 cnt = 1

    #             if i == len(nums) - 1:
    #                 # print(cnt)
    #                 if cnt >= 2:
    #                     sum += self.n_count(cnt - 1)
    #         return sum

    #     def n_count(self, n):
    #         return n * (n + 1) / 2


sol = Solution()
nums = [1, 2, 3, 77, 4, 5, 6]
# nums = [-1, -2, -3]
resp = sol.numberOfArithmeticSlices(nums)
print(resp)
