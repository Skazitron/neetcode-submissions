class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        n = len(s)

        t_count = Counter(t)
        s_cur = defaultdict(int)
        have = 0
        need = len(t_count)
        r = 0
        print(need)

        indices = [-1, -1]
        mn = float('inf')
        for i,x in enumerate(s):
            while (need > have and r < n):
                if s[r] in t_count:
                    s_cur[s[r]] += 1
                    if s_cur[s[r]] == t_count[s[r]]:
                        have += 1
                    print(s_cur[x], t_count[x])
                r += 1

            if (need == have):
                if r - i < mn:
                    indices = [i, r]
                    mn = r - i
            
            if (t_count[x]):
                s_cur[x] -= 1
                if s_cur[x] < t_count[x]:
                    have -= 1

        i,j = indices
        if i != -1 and j != -1:
            return s[i:j]

        else: return ""