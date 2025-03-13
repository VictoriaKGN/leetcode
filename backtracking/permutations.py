# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, options):
            if len(options) == 0:
                res.append(path[:])
                return

            for i in range(len(options)):
                new_options = options[:i] + options[i+1:]
                path.append(options[i])
                dfs(path, new_options)
                path.pop()

        dfs([], nums)

        return res


