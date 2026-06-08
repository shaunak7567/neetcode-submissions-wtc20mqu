class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """ Dont return anything, modify in place """
        # 1. [DFS] Capture unsurrounded regions ( covert O to T)
        # 2. Capture surrounded regions (O to X)
        # 3. Upcapture unsurrounded regions(T to O)

        ROWS,COLS = len(board), len(board[0])
        def capture(r,c):
            if (r<0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return 
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
               if (board[r][c] == "O" and (r in [0,ROWS-1] or c in [0,COLS-1])):
                capture(r,c) 
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"