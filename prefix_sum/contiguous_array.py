class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        diffs = {}
        zeros = 0
        ones = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1

            diff = ones - zeros

            if diff not in diffs:
                diffs[diff] = i
        
            if diff == 0 :
                res = zeros + ones
            else:
                res = max(res, i - diffs[diff])
   
        return res