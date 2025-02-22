# 34. Find First and Last Position of Element in Sorted Array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(self, left_bias):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) //2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    index = mid
                    if left_bias:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return index

        left = binary_search(self, True)
        right = binary_search(self, False)
        return [left, right]
        