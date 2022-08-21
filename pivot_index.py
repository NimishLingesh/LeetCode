from typing import List

class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    #     sum_total = sum(nums)
    #     for idx, i in enumerate(nums):
    #         if idx == 0:
    #             left = 0
    #             right = sum(nums[1:])
    #         elif idx == len(nums)-1:
    #             right = 0
    #             left = sum(nums[:-1])
    #         else:
    #             left = sum(nums[:idx])
    #             # right = sum(nums[idx+1:])
    #             right = sum_total - (left + i)
    #         if left == right:
    #             return idx
    #     return -1
        
    def pivotIndex(self, nums: List[int]) -> int:
        sum_total = sum(nums)
        for idx, i in enumerate(nums):
            if idx == 0:
                left = 0
                right = sum(nums[1:])
            else:
                left += nums[idx-1]
                right -= i
            if left == right:
                return idx
        return -1


sol = Solution()
nums = [2,1,-1]
print(sol.pivotIndex(nums))