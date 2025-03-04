class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        
        def dfs_mark(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != "O":
                return

            board[r][c] = "#"

            dfs_mark(r - 1, c)
            dfs_mark(r + 1, c)
            dfs_mark(r, c - 1)
            dfs_mark(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    dfs_mark(r, c)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"