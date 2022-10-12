class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        return self.helper(nums, 3, target)
        
    def helper(self, nums, k, target):
        closest = nums[:k]
        for i, x in enumerate(nums[:-k+1]):
            current = x + self.helper(nums[i+1:], k-1, target-x)
            if abs(target - current) < abs(target - closest):
                closest = current
        return closest