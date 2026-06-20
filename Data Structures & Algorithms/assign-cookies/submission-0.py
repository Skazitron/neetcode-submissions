class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gi = len(g) - 1
        si = len(s) - 1

        cnt = 0
        while (gi > -1 and si > -1):
            if s[si] >= g[gi]:
                cnt += 1
                si -= 1
                gi -=1
            else:
                gi-=1

        return cnt