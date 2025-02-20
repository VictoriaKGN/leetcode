class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(s) < len(p):
            return []
        
        p_freq = {}
        window = {}
        res = []

        for i in range(len(p)):
            p_freq[p[i]] = p_freq.get(p[i], 0) + 1
            window[s[i]] = window.get(s[i], 0) + 1

        if window == p_freq:
            res.append(0)

        for right in range(len(p), len(s)):
            outgoing = right - len(p)
            window[s[outgoing]] -= 1
            if window[s[outgoing]] == 0:
                window.pop(s[outgoing])
                
            window[s[right]] = window.get(s[right], 0) + 1
            
            if window == p_freq:
                res.append(outgoing + 1)

        return res

solution = Solution()
solution.findAnagrams("cbaebabacd", "abc")