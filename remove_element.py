class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for idx, i in enumerate(nums):
            if i == val:
                count += 1
                nums.pop(idx)
        for j in range(count):
            nums.append("_")
        return nums


sol = Solution()
nums = [3, 2, 2, 3]
val = 3
res = sol.removeElement(nums, val)
print(res)
