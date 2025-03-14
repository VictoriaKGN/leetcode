# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, path):
            if start == len(nums):
                res.append(path[:])
                return

            path.append(nums[start])
            dfs(start + 1, path)

            path.pop()
            dfs(start + 1, path)

        dfs(0, [])

        return res