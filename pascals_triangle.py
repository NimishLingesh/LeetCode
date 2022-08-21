class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for row in range(0,numRows):
            ele = []
            for col in range(0,row+1):
                if (col == 0 or col == row):
                    ele.append(1)
                else:
                    # ele.append(0)
                    num = res[row-1][col-1] + res[row-1][col]
                    ele.append(num)
            res.append(ele)
        return res
            # print(ele)
            # print(" ")
        

sol = Solution()
print(sol.generate(5))