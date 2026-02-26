class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        cols = set()
        rdiag = set()
        ldiag = set()
        board = [['.']*n for _ in range(n)]
        def check(r):
            if(r == n):
                copy = ["".join(row) for row in board]
                solutions.append(copy)
                return
            #scorro le colonne e piazzo la regina se non è gia presente in qujella colonna o nelle diagonali
            for c in range(n):
                if((c in cols) or ((r+c) in rdiag) or (r-c) in ldiag):
                    continue

                cols.add(c)
                rdiag.add(r+c) 
                ldiag.add(r-c)

                board[r][c] = 'Q'
                check(r + 1)

                cols.remove(c)
                rdiag.remove(r+c)
                ldiag.remove(r-c)
                board[r][c] = '.'
        check(0)
        return solutions
             

                

        