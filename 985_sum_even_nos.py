class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        res = []
        s = 0
        for num in nums:
            if num % 2 == 0:
                s += num
        for q in queries:
            idx = q[1]
            prev = nums[idx]
            nums[idx] = q[0] + nums[idx]
            if prev % 2 == 0 and nums[idx] % 2 ==0:
                diff = q[0]
                s += diff
            elif prev % 2 == 0 and nums[idx] % 2 != 0:
                s -= prev
            elif nums[idx] % 2 == 0:
                s += nums[idx]
            res.append(s)
        return res

sol = Solution()
nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(sol.sumEvenAfterQueries(nums, queries))