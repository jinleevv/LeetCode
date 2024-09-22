class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for cord in points:
            distance = ((0 - cord[0])**2 + (0 - cord[1])**2)**0.5
            result.append((distance, cord))
        
        heapq.heapify(result)
        ans = []
        while k != 0:
            k -= 1
            ans.append(heapq.heappop(result)[1])

        return ans