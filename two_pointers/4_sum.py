class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = len(nums) - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
                    
        return res