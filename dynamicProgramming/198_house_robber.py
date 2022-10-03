class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
        """if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) > 2:
            return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        else:
            return max(nums[0], nums[1])"""
        
            