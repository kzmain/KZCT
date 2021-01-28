class Solution:
    cnt = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0:
            return 0
        board = [[1 for _ in range(n)] for _ in range(m)]
        l_bound, t_bound = -1, -1
        r_bound, b_bound = n, m
        self.cnt = 0

        def dfs(_row, _col):
            if (_row == t_bound) \
                    or (_row == b_bound) \
                    or (_col == l_bound) \
                    or (_col == r_bound):
                return
            if board[_row][_col] == 0:
                return
            sum_checker = 0
            for num in [_row, _col]:
                while num >= 10:
                    sum_checker += num % 10
                    num //= 10
                sum_checker += num
            if sum_checker > k:
                return
            board[_row][_col] = 0
            self.cnt += 1
            dfs(_row + 1, _col)
            dfs(_row - 1, _col)
            dfs(_row, _col + 1)
            dfs(_row, _col - 1)

        for row in range(m):
            for col in range(n):
                dfs(0, 0)
        return self.cnt

so = Solution()
print(so.movingCount(2, 3, 1))
print(so.movingCount(5, 4, 0))
