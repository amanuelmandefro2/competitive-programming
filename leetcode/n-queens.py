class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        left_diagonal, right_diagonal = set(), set()
        column = set()
        ans = []
        board = [['.' for c in range(n)] for r in range(n)]
       
        def backtrack(r, board):
            if r == n:
                new_board = []
                for value in board:
                    new_board.append(''.join(value))
                ans.append(new_board)
                return 

            for c in range(n):
                if c in column or r - c in right_diagonal or r+c in left_diagonal:
                    continue
                column.add(c)
                right_diagonal.add(r-c)
                left_diagonal.add(r+c)
                board[r][c] = 'Q'
                backtrack(r+1, board)
                column.remove(c)
                right_diagonal.remove(r-c)
                left_diagonal.remove(r+c) 
                board[r][c] = '.'
        backtrack(0, [['.' for c in range(n)] for r in range(n)])            

        return ans          


        