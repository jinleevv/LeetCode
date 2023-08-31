class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())