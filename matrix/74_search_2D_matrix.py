class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row = self.binarySearch(matrix[:][0], target)

    def binarySearch(self, mat_list, target):
        

        

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))