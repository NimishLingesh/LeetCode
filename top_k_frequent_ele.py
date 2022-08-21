class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        for ele in nums:
            if ele not in nums_dict.keys():
                nums_dict[ele] = [1, ele]
            else:
                nums_dict[ele][0] += 1
        # sort = dict(sorted(nums_dict.items(), key=lambda item: item[1]))
        l = sorted(nums_dict.values())[-k:]
        l2 = [l1[1] for l1 in l]
        return l2


sol = Solution()
nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 1]
k = 2
print(sol.topKFrequent(nums, k))
