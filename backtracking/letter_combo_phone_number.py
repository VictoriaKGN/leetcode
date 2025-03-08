# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

        if not digits:
            return []
        
        res = []

        def dfs(start_digit, path):
            if start_digit == len(digits):
                res.append("".join(path))
                return

            for char in digits_map[digits[start_digit]]:
                path.append(char)
                dfs(start_digit + 1, path)
                path.pop()

        dfs(0, [])

        return res
            