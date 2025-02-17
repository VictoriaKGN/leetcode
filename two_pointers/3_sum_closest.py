class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        res = float('inf')
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(res - target):
                    res = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total
        
        return res