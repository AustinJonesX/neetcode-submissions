class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_hash = {[set(), set(), set()]}

        for i in range(len(board)):
            for j in range(board()):
                num = board[i][j]
                