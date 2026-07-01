class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        first = set(nums)


        def permute(s, arr):
            if not s:
                ret.append(arr)
            else:
                for x in s:
                    temp = s.copy()
                    temp.remove(x)
                    temparr = arr[:]
                    temparr.append(x)
                    permute(temp, temparr)
        permute(first, [])
        return ret
        