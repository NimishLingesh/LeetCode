class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        nums_len = len(nums)
        dict_n = {}
        print(nums_len)
        for idx in range(nums_len):
            if nums[idx] in dict_n:
                if abs(dict_n[nums[idx]] - idx) <= k:
                    return True
            else:
                dict_n[nums[idx]] = idx
        return False

sol = Solution()
nums = [1,0,1,1]
k = 1
print(sol.containsNearbyDuplicate(nums, k))