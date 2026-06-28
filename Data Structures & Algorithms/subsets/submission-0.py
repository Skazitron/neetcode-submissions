class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(start, cur):
            ret.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        backtrack(0, [])
        return ret