import pdb


class Solution:
    def largestPerimeter(self, nums) -> int:
        nums = sorted(nums, reverse=True)
        print(nums)
        peri = 0
        for idx, win in enumerate(nums[:-2]):
            if nums[idx+1] + nums[idx+2] > win:
                l_peri = win + nums[idx+1] + nums[idx+2]
                if l_peri > peri:
                    peri = l_peri
        return peri
            
sol = Solution()
nums = [3,2,3,4]
print(sol.largestPerimeter(nums))