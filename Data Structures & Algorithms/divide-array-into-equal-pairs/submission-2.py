class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = Counter(nums)
        pairs = 0
        for num, cnt in s.items():
            if cnt % 2 != 0:
                return False
        return True