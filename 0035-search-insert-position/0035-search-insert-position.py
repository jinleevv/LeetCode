class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pivot = left + (right - left) / 2

        while left <= right:
            pivot = left + (right - left) / 2

            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1

        return left