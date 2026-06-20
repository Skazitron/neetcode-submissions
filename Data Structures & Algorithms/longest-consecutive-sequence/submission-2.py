class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for x in s:
            cur = 1
            y = x - 1
            while (y in s):
                cur += 1
                y-=1
            mx = max(mx, cur)
        return mx