class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        size = len(nums)
        for i in range(size):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] = numsDict[nums[i]] + 1
                
            if numsDict[nums[i]] >= (size / 2):
                return nums[i]


