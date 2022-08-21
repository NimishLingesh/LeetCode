class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        aggr = []
        for idx, row in enumerate(mat):
            soldier = 0
            civil = 0
            for col in row:
                if col == 1:
                    soldier += 1
                else:
                    civil += 1
            aggr.append([soldier, civil, idx])
        print(aggr)
        aggr.sort()

        result = []
        for i in range(0, k):
            result.append(aggr[i][2])

        return result


sol = Solution()
mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
k = 2
res = sol.kWeakestRows(mat, k)
print(res)
