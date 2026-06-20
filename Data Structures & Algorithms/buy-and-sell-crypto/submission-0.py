class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = prices[0]
        prof = 0

        for x in prices:
            prof = max(prof, x - mn)
            mn = min(x, mn)
            
        return prof

