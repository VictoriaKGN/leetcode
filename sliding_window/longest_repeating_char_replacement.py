class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        freq = {}
        res = 0
        i = 0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            curr_len = j - i + 1
            max_freq = max(freq.values())

            if curr_len - max_freq > k:
                freq[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)

        return res
