class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if (len(matrix) == 0) or (len(matrix[0]) == 0):
            return False
        col = len(matrix[0]) - 1
        row = 0

        col_bound = -1
        row_bound = len(matrix)
        while (col != col_bound) and (row != row_bound):
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True