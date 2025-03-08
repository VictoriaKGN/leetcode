# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates, target): 
        res = []

        def dfs(index, path, path_sum):
            if path_sum == target:
                res.append(path[:])
                return

            if path_sum < target and index < len(candidates):
                path.append(candidates[index])
                dfs(index, path, path_sum + candidates[index])
                path.pop()

                dfs(index + 1, path, path_sum)

        dfs(0, [], 0)

        return res
    
solution = Solution()
solution.combinationSum([2,3,6,7], 7)