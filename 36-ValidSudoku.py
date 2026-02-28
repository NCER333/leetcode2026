class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(row, col, number):
            for i in range(9):
                if(board[row][i] == number and i != col):
                    return False
            for j in range(9):
                if(board[j][col] == number and j != row):
                    return False
            #sottoquadrato 3x3
            colzone = col // 3
            rowzone = row // 3
            startrow = rowzone * 3
            startcol = colzone * 3
            for i in range(startrow, startrow + 3):
                for j in range(startcol, startcol + 3):
                    if(board[i][j] == number and i != row and j != col):
                                return False

            return True
        
        
        for i in range(9):
            for j in range(9):
                if(board[i][j] == '.'):
                    continue
                else:
                    valid = check(i, j, board[i][j])
                    if(not valid):
                        return False
        return True #se attraversa tutta la tabella senza problemi