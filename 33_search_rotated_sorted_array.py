class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # analyse the solution again, Neetcode soln
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1

        # Not completely correct
        """nums_cpy = nums.copy()
        nums_sort = sorted(nums)
        pivot = 0
        # for idx, num in enumerate(nums):
        #     if num != nums_cpy[idx]:
        #         pivot = idx
        pivot = nums_cpy.index(nums_sort[0])
        # print("pivot", pivot)
        res = self.binary(nums_sort, 0, len(nums)-1, target)
        if res == -1:
            return res
        else:
            if res < pivot:
                return res + pivot
            else:
                return res - pivot
        
    def binary(self, nums, first, last, target):
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
        return -1
        """