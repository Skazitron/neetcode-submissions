class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i,x in enumerate(strs):
            reord = "".join(sorted(list(x)))
            m[reord].append(i)

        res = []
        for x in m.values():
            rar = []
            for idx in x:
                rar.append(strs[idx])
            res.append(rar)
        
        return res
        
