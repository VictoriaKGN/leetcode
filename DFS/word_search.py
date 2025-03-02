class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if 0 <= r and r < rows and 0 <= c and c < cols and board[r][c] == word[i]:
                temp = board[r][c]
                board[r][c] = "#"
                res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
                board[r][c] = temp 
                return res

            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False