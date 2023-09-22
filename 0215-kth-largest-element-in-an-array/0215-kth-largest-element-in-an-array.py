class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            number = -1 * num
            heappush(maxHeap, number)

        while k > 0:
            large = heappop(maxHeap)
            print(large)
            k -= 1
            
        return -1*large