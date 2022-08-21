class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diffs = []
        for c1, c2 in costs:
            diff = c1 - c2
            # if c1 < c2:
            diffs.append([diff, c1, c2])
        sum = 0
        diffs.sort()
        # print(diffs)
        for ind, i in enumerate(diffs):
            if ind < len(diffs) // 2:
                sum += i[1]
            else:
                sum += i[2]

        return sum


sol = Solution()
costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
sum = sol.twoCitySchedCost(costs)
print(sum)
