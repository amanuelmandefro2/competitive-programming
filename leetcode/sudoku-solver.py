class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def find_pos():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        return [r,c]
            return [-1, -1]

        def isvalid(r,c,num):
            for i in range(9):
                if board[i][c] == num:
                    return False
                if board[r][i] == num:
                    return False
            
            start_r = (r //3) *3
            start_c = (c//3) *3

            for i in range(3):
                for j in range(3):
                    if board[i + start_r][j + start_c] == num:
                        return False
            return True

        def validsudoku():
            row,col = find_pos()
            if row == -1 and col == -1:
                return True
            
            for i in "123456789":
                if isvalid(row,col,i):
                    board[row] [col] = i
                    if validsudoku():
                        return True
                    board[row][col] = '.'
            return False

        validsudoku()                      

    