class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = self.cal_mid(left, right)
        index = self.recurse(left, right, mid, nums, target)
        return index

    def recurse(self, left, right, mid, nums, target):
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        if left > right:
            return -1
        mid = self.cal_mid(left, right)
        return self.recurse(left, right, mid, nums, target)

    def cal_mid(self, left, right):
        sum = left + right
        if sum % 2 == 1:
            mid = int(sum / 2) + 1
        else:
            mid = sum / 2
        return mid

    #     if len(nums) == 0:
    #         return -1
    #     tmp = True
    #     left = 0
    #     right = len(nums) - 1
    #     # if left == right:
    #     #     return -1
    #     while tmp:

    #         resp, mid = self.find_num(left, right, target, nums)
    #         # import pdb

    #         # pdb.set_trace()
    #         if resp == 0:
    #             return mid
    #         if left == right or mid == right or mid == left:
    #             return -1
    #         if resp == -1:
    #             right = mid
    #         elif resp == 0:
    #             tmp = False
    #         elif resp == 1:
    #             left = mid
    #         else:
    #             return -1

    #     return mid

    # def find_num(self, left, right, target, nums):
    #     sum = left + right
    #     if sum % 2 == 1:
    #         mid = int(sum / 2) + 1
    #     else:
    #         mid = sum / 2
    #     if nums[mid] == target:
    #         return 0, mid
    #     elif nums[left] == target:
    #         return 0, left
    #     elif target < nums[mid]:
    #         return -1, mid
    #     else:
    #         return 1, mid


sol = Solution()
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
target = 2
index = sol.search(nums, target)
print(index)
