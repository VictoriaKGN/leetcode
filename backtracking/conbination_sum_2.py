# 40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(index, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                    
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)

        return res
    
solution = Solution()
solution.combinationSum2([10,1,2,7,6,1,5], 8)