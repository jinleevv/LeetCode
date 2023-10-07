class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}
        included = []
        result = ""

        s_list = s.split(" ")
        index = 0

        if len(s_list) != len(pattern):
            return False

        for i in range(len(s_list)):
            if pattern[i] not in patterns and s_list[i] not in included:
                patterns[pattern[i]] = s_list[i]
                included.append(s_list[i])

        for i in range(len(pattern)):
            print(pattern[i])
            if pattern[i] not in patterns:
                return False
            else:
                if index == 0:
                    result = result + patterns[pattern[i]]
                    index += 1
                else:
                    result = result + " " + patterns[pattern[i]]
        
        if result == s:
            return True
        return False