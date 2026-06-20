class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        t_c = Counter(t)

        if len(s_c) != len(t_c):
            return False

        for char, cnt in s_c.items():
            if t_c[char] != cnt:
                return False
        return True