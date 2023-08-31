class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        StringX = str(x)
        if len(StringX) % 2 == 0:
            length = len(StringX) / 2
            return StringX[:length] == (StringX[length:])[::-1]
        else:
            length = (len(StringX) / 2)
            return StringX[:length] == (StringX[length + 1:])[::-1]