class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = [c.lower() for c in s if c.isalnum()]
        # return all (s[i] == s[~i] for i in range(len(s)//2))

        # filtered_chars = filter(lambda ch: ch.isalnum(), s)
        # lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        # filtered_chars_list = list(lowercase_filtered_chars)
        # reversed_chars_list = filtered_chars_list[::-1]

        # return filtered_chars_list == reversed_chars_list

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True