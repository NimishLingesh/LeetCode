class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max = 0
        # for idx, i in enumerate(prices):
        #     for j in prices[idx:]:
        #         if j>i:
        #             diff = j-i
        #             if diff>max:
        #                 max = diff
        # return max

        # max = 0
        # prices_cpy = prices
        # for idx, i in enumerate(prices):
        #     sub_arr = prices_cpy[idx:]
        #     import pdb
        #     pdb.set_trace()
        #     j = max(sub_arr)
        #     if j>i:
        #         diff = j-i
        #         if diff>max:
        #             max = diff
        # return max

        # max_num = 0
        # for idx, i in enumerate(prices):
        #     sub_arr = prices[idx:]
        #     max_var = max(sub_arr)
        #     if max_var<i:
        #         return max
        #     for j in prices[idx:]:
        #         if j>i:
        #             diff = j-i
        #             if diff>max_num:
        #                 max_num = diff
        # return max_num
        max_num = 0
        min_num = prices[0]
        for idx, i in enumerate(prices):
            min_num = min(min_num, i)
            max_num = max(max_num, i-min_num)
        return max_num


sol = Solution()
prices = [7,1,5,3,6,4]

print(sol.maxProfit(prices))