# 567. Permutation in String

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False

        window = {}
        s1_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == s1_map:
            return True

        for left in range(len(s2) - len(s1)):
            right = left + len(s1)

            outgoing = s2[left]
            window[outgoing] -= 1
            if window[outgoing] == 0:
                window.pop(outgoing)

            incoming = s2[right]
            window[incoming] = window.get(incoming, 0) + 1

            if window == s1_map:
                return True

        return False
           
solution = Solution()
solution.checkInclusion("ab", "eidbaooo")
        
