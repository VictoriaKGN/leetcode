# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        res = []

        def dfs(left, right, path):
            if left == n and right == n:
                res.append("".join(path))
                
            if left < n:
                path.append("(")
                dfs(left + 1, right, path)
                path.pop()

            if right < n and right < left:
                path.append(")")
                dfs(left, right + 1, path)
                path.pop()

        dfs(0, 0, [])

        return res