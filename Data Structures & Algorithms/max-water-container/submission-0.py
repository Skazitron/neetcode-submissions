class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mx = 0
        while (l < r):
            lh = heights[l]
            rh = heights[r]
            width = r - l
            cur = width*min(lh, rh)
            mx = max(mx, cur)
            if lh <= rh:
                l += 1
            elif rh < lh:
                r -= 1
        return mx