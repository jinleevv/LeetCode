class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = {}
        res = 0
        
        for task in tasks:
            if task not in frequency:
                frequency[task] = 1
            else:
                frequency[task] += 1
        
        for key, value in frequency.items():
            if value == 1:
                return -1
            
            if value % 3 == 0:
                res += value // 3
            else:
                res += value // 3 + 1
                
        
        return res