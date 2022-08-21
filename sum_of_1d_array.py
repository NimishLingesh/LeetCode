class Solution:
    def runningSum(self, nums):
        arr = []
        # if len(nums) < 2:
        #     return nums
        for idx, i in enumerate(nums):
            if idx > 0:
                nums[idx] += nums[idx-1]
        return nums

sol = Solution()
nums = [1,2,3,4]
print(sol.runningSum(nums))