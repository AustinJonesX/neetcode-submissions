class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [] * 9
        cols = [] * 9
        squares = [] * 9

        for r in range(9):
            for c in range(9):
                num = val(board[r][c]) - 1

                if (1 << num) & rows[r]:
                    return False
                if (1 << num) & cols[c]:
                    return False
                if (1 << num) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << num)
                cols[c] |= (1 << num)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << num)
        return True