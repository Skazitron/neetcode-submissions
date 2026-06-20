class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = Counter(nums)

        for k,v in s.items():
            if v%2 != 0:
                return False

        return True