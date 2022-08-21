from tkinter import W
from typing import List


class Solution:
    def __init__(self):
        self.d_time = {}
        self.max = -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mat = [[0 for i in range(n)] for j in range(n)]
        for row in times:
            # for start, end, w in row:
            # print(row)
            r = row[0] - 1
            c = row[1] - 1
            mat[r][c] = row[2]
        k = k - 1
        # q = []
        # q.append(k)
        self.d_time[k] = mat[k][k]
        # while len(q):
        #     u = q.pop(0)
        #     for c_idx, weight in enumerate(mat[u]):
        #         if mat[u][c_idx]:
        #             visited[c_idx] = mat[u][c_idx]
        #             q.append(c_idx)

        # visit each col in row k
        # for i in range(n):
        # check if the visiting ele is not already present in d_time dict
        # if mat[k][i] and not self.d_time.get(i, 0):
        #     self.d_time[i] = mat[k][i]

        stac = [k]
        prev = k
        while len(stac):
            u = stac.pop(0)

            for i in range(n):
                if mat[u][i]:
                    # if u != k:
                    #     self.d_time[i] =
                    stac.append(i)
                    if self.d_time.get(i):
                        # self.d_time[i] += mat[u][i]
                        continue
                    else:
                        self.d_time[i] = mat[u][i] + mat[prev][u]
            prev = u
        print(self.d_time)
        if len(self.d_time.keys()) < n:
            return -1
        else:
            return max(self.d_time.values())


sol = Solution()
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(sol.networkDelayTime(times, n, k))
