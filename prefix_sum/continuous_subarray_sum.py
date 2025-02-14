class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            val = nums[i]
            total += val
            remainder = total % k
            if remainder not in mod_seen:
                mod_seen[remainder] = i
            else:
                if i - mod_seen[remainder] > 1:
                    return True

        return False
