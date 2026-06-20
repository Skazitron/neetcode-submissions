class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lastMap = {}
        maxDistance = 0
        l = 0

        for i,x in enumerate(s):
            if x in lastMap:
                l = max(lastMap[x] + 1, l)
            maxDistance = max(maxDistance,i-l+1)
            # print(s[l: i+1], maxDistance)
            lastMap[x] = i
        
        return  maxDistance