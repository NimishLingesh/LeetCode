class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        sum = 0
        local_min = sum(neededTime)
        for idx, i in enumerate(colors):
            if idx == len(colors)-1:
                break
            if i == colors[idx+1]:
                local_min = min(local_min, min(neededTime[idx], neededTime[idx+1]))
        return sum
        

sol = Solution()
colors = "aaabbbabbbb"
neededTime = [3,5,10,7,5,3,5,5,4,8,1]
print(sol.minCost(colors, neededTime))