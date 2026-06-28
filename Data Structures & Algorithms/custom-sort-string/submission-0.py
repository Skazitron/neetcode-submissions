class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = Counter(s)

        res = []
        for c in order:
            if c in s:
                res.append(c * s[c])
                del s[c]

        for k, v in s.items():
            res.append(k * v)
        
        return "".join(res)
        

        