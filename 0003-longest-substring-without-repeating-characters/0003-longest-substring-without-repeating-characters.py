class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        duplicates = set()
        
        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])
            maxLength = max(r - l + 1, maxLength)
        
        return maxLength