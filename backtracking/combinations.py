# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path, start):
            if len(path) == k:
                res.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                dfs(path, num + 1)
                path.pop()

        dfs([], 1)

        return res