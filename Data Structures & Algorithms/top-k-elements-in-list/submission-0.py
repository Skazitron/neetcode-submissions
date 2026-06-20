class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)

        res = []
        for key,val in s.items():
            res.append([val, key])
        
        res.sort()

        rarr = []
        
        for x,y in res[-k:]:
            rarr.append(y)
        return rarr