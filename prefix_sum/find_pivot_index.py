class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i

        return -1       