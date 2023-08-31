class Solution(object):
    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)
        # reverse each word
        self.reverse_each_word(s)
        
    # def reverseWords(self, s):
    #     """
    #     :type s: List[str]
    #     :rtype: None Do not return anything, modify s in-place instead.
    #     """
    #     left = 0
    #     right = len(s) - 1

    #     start = 0
    #     flipend = 0
    #     end = 0

    #     while left < right:
    #         temp = s[left]
    #         s[left] = s[right]
    #         s[right] = temp

    #         left += 1
    #         right -= 1

    #     while end < len(s):
    #         if s[end] == " ":
    #             flipend = end - 1

    #             while start < flipend:
    #                 temp = s[start]
    #                 s[start] = s[flipend]
    #                 s[flipend] = temp
    #                 start += 1
    #                 flipend -= 1

    #             start = end + 1

    #         if end == len(s) - 1:
    #             flipend = len(s) - 1
    #             while start < flipend:
    #                 temp = s[start]
    #                 s[start] = s[flipend]
    #                 s[flipend] = temp
    #                 start += 1
    #                 flipend -= 1

    #         end += 1
        