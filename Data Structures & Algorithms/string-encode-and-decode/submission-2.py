class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append(':')
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = s.find(':', i)
            if j == -1:
                break
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res