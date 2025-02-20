class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        window = {}
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window.pop(s[left])
                left += 1
            window[s[right]] = right
            print(window)
            res = max(res, len(window.keys()))

        return res
    
solution = Solution()
solution.lengthOfLongestSubstring("pwwkew")