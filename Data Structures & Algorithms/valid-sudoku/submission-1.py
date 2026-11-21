class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]

            if num in rows[i]:
                return False
            if num in cols[i]:
                return False
            if num in squares[(i,j)]:
                return False

            rows[i].append(num)
            cols[j].append(num)
            squares[(i,j)].append(num)
        
        return True