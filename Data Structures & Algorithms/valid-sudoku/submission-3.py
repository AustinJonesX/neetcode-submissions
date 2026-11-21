class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                if num in rows[i]:
                    return False
                if num in cols[i]:
                    return False
                if num in squares[(i // 3, j // 3)]:
                    return False

                rows[i].append(num)
                cols[j].append(num)
                squares[(i,j)].append(num)
        
        return True