class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, x in enumerate(nums):
            if (target-x) in m:
                j = m.get(target-x)
                return [j, i]
            else:
                m[x] = i
        return [-1, -1]