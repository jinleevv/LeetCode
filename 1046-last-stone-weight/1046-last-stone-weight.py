class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        smash = []
        heapq.heapify(smash)

        for stone in stones:
            heapq.heappush(smash, -stone)
        
        while True:
            if len(smash) == 1:
                break
            if len(smash) == 0:
                return 0

            if len(smash):
                x = -heapq.heappop(smash)
                y = -heapq.heappop(smash)

            if x < y:
                heapq.heappush(smash, -(y - x))
            elif x > y:
                heapq.heappush(smash, -(x - y))


        return -heapq.heappop(smash)