class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l = [''] * len(s)
        r = [''] * len(t)

        for i in range(len(s)):
            l[i] = s[i]

        for i in range(len(s)):
            r[i] = t[i]

        l.sort()
        r.sort()

        for i in range(len(s)):
            if l[i] != r[i]:
                return False
            

        return True