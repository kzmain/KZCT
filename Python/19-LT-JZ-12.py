from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        l_bound, r_bound, t_bound, b_bound = -1, 0, -1, 0
        b_bound = len(board)
        r_bound = len(board[0])
        w_len = len(word)

        def dfs(word_loc, _row, _col):
            if word_loc == w_len:
                return True
            if (_row == t_bound) \
                    or (_row == b_bound) \
                    or (_col == l_bound) \
                    or (_col == r_bound) \
                    or (board[_row][_col] != word[word_loc]):
                return False
            tmp, board[_row][_col] = board[_row][_col], ""
            word_loc += 1
            rst = dfs(word_loc, _row + 1, _col) or dfs(word_loc, _row - 1, _col) or dfs(word_loc, _row, _col + 1) or dfs(word_loc, _row, _col - 1)

            board[_row][_col] = tmp
            return rst

        for row in range(b_bound):
            for col in range(r_bound):
                if dfs(0, row, col):
                    return True
        return False


so = Solution()
print(so.exist([["a", "a"]], "aaa")) 