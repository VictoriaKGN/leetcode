class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) <= 10:
            return []

        window = []
        res = []
        seen = {}

        for right in range(10, len(s) + 1):
            left = right - 10
            window = s[left:right]

            # if window in seen:
            seen[window] = seen.get(window, 0) + 1
            if seen[window] == 2:
                res.append(window)

        return res


solution = Solution()
solution.findRepeatedDnaSequences("CAAAAAAAAAA")