class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        # [10,15,20] 0

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])


    # def __init__(self) -> None:
    #     import sys
    #     self.min_cost = sys.maxsize

    # def minCostClimbingStairs(self, cost):
    #     # if len(cost) < 1:
    #     #     return 0
    #     # elif len(cost) == 1:
    #     #     return 0
    #     # if cost[0] < cost[1]:
    #     #     idx = 1
    #     # else:
    #     #     idx = 2
    #     # return min(cost[0], cost[1]) + self.minCostClimbingStairs(cost[idx:])
    #     cost.append("end")
    #     total_sum = 0
    #     self.recurse(cost, total_sum)
    #     return self.min_cost

    # def recurse(self, cost, total_sum):
    #     if cost[0] == "end":
    #         self.min_cost = min(self.min_cost, total_sum)
    #     return total_sum + min(self.recurse(cost[1:], total_sum+cost[0]), self.recurse(cost[2:], total_sum+cost[1]))
 


sol = Solution()
cost = [10,15,20]
print(sol.minCostClimbingStairs(cost))
