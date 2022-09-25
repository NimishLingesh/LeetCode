class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

        """
        row = self.searchRow(matrix, target)
        if row == None:
            # print("row is none")
            return False
        return self.searchCol(row, target)

    def searchRow(self, mat_list, target):
        begin = 0
        total_len = len(mat_list)
        while(begin <= total_len):
            # import pdb 
            # pdb.set_trace()

            mid = (total_len + begin)//2
            if len(mat_list[mid]) == 1:
                last_idx = 0
            elif len(mat_list[mid]) == 1 and target != mat_list[mid][0]:
                return False
            else:
                last_idx = -1

            if target >= mat_list[mid][0] and target <= mat_list[mid][last_idx]:
                return mat_list[mid]
            elif target > mat_list[mid][0]:
                begin = mid + 1
            elif target < mat_list[mid][0]:
                total_len = mid - 1
        return None

    def searchCol(self, row, target):
        first = 0
        last = len(row)
        while(first <= last):
            mid = (first + last)//2
            if target == row[mid]:
                return True
            elif target > row[mid]:
                first = mid + 1
            elif target < row[mid]:
                last = mid - 1
        return False
"""

sol = Solution()
matrix = [[1]]
target = 13
print(sol.searchMatrix(matrix, target))