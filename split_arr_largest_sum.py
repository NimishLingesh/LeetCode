class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # nums = sorted(nums)
        min_val = max(nums)
        max_val = sum(nums)
        min_sum = 9999999
        # return [min_val, max_val]
        if len(nums) == m:
            return max(nums)
        while min_val <= max_val:
            temp = []
            mid = (min_val + max_val) // 2

            n_sum = 0
            for i in nums:
                n_sum += i
                if n_sum > mid:
                    temp.append(n_sum - i)
                    n_sum = i
                if i == nums[-1]:
                    temp.append(n_sum)
            # print(min_val, mid, max_val, temp)
            if len(temp) == m:
                # print("Max of temp : ", max(temp))
                min_sum = min(min_sum, max(temp))
                max_val = ((min_val + max_val) // 2) - 1
                # max_val -= 1
            elif len(temp) > m:
                min_val = ((min_val + max_val) // 2) + 1
            else:
                max_val = ((min_val + max_val) // 2) - 1

        return min_sum


sol = Solution()
nums = [2, 16, 14, 15]
m = 2
lar_sum = sol.splitArray(nums, m)
print(lar_sum)
