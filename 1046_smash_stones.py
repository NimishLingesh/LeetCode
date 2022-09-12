class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            s1 = stones.pop(-1)
            s2 = stones.pop(-1)
            diff = abs(s1-s2)
            if diff != 0:
                stones.append(diff)
            # print(stones)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0

sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))