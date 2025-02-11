class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        sufix = [0] * len(nums)
        sufix[-1] = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i]

        nums[0] = sufix[1]
        nums[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            nums[i] = prefix[i - 1] * sufix[i + 1]

        return nums