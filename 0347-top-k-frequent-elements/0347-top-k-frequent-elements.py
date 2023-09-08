class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1
        
        store = sorted(store.items(), key=lambda x: x[1], reverse=True)
        store = store[:k]
        for i in range(len(store)):
            store[i] = store[i][0]

        return store
            