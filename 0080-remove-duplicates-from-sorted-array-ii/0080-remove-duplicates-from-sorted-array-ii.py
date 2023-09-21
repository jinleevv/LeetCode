class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate = {}

        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate[nums[i]] = 1
            elif nums[i] in duplicate:
                    duplicate[nums[i]] += 1

        for key, value in duplicate.items():
            if value >= 2:
                while value > 2:
                    nums.remove(key)
                    value -= 1

        
        