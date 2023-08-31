class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in store:
                return [i, store[x]]
            else:
                store[nums[i]] = i

        return []