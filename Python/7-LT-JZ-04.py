class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if (len(matrix) == 0) or (len(matrix[0]) == 0):
            return False
        l_start = 0
        r_bound = len(matrix[0])
        t_start = 0
        b_bound = len(matrix)
        for row in range(t_start, b_bound):
            for col in range(l_start, r_bound):
                if matrix[row][col] == target:
                    return True
                if matrix[row][col - 1] < target < matrix[row][col]:
                    r_bound = col
                    break
        return False