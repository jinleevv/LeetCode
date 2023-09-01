class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)
        count = {}

        for x in s:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        for x in t:
            if x in count:
                count[x] -= 1
            else:
                return False

        for key, value in count.items():
            if value != 0:
                return False

        return True

        
        
        