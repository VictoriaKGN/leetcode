# 131. Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(string):
            return string == string[::-1]

        def dfs(start, path):
            if start >= len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    dfs(end, path)
                    path.pop()

        dfs(0, [])

        return res