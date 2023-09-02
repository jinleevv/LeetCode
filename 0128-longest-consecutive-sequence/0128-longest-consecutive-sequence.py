class Solution:
    def longestConsecutive(self, nums: List[int]):
        if nums == []:
            return 0

        high = len(nums) - 1

        # self.quicksort(nums, 0, high)
        nums.sort()

        consecutive = 1
        current = 1

        for i in range(1, len(nums)):
            prev = nums[i] - 1
            if nums[i] == nums[i-1]:
                continue
            if prev == nums[i-1]:
                current += 1
                if current >= consecutive:
                    consecutive = current
            else:
                current = 1

        return consecutive

            