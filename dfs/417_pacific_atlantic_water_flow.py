# NOT SOLVED YET
class Solution:
    def pacificAtlantic(self, heights) :
        def check_for_
        res = []
        for r_idx, row in enumerate(heights):
            for c_idx, col in enumerate(row):
                pacific = 0
                atlantic = 0
                r_local = r_idx
                c_local = c_idx
                while r_local >= 0 and r_local <=len(row) and c_local >=0 and c_local <= len(heights):

            

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
sol.pacificAtlantic(heights)