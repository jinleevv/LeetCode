class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}

        for x in nums:
            if x in count:
                return True
            else:
                count[x] = 1

        return False