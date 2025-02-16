class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        curr_sum = 0
        sums = {0: 1}
        res = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            
            diff = curr_sum - k
            if diff in sums:
                res += sums[diff]

            sums[curr_sum] = sums.get(curr_sum, 0) + 1

        return res