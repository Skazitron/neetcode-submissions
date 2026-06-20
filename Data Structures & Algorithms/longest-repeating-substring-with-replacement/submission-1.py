class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = set(s)
        n = len(s)
        mx = 0

        for x in unique:
            l = 0
            cnt = k 
            
            for r in range(n):
                if s[r] != x:
                    cnt -= 1
                
                while cnt < 0:
                    if s[l] != x:
                        cnt += 1
                    l += 1
                
                mx = max(mx, r - l + 1)

        return mx