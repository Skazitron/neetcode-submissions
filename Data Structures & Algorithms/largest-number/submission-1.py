import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        str_list = [str(x) for x in nums]

        def comparator(a, b):
            if a+b>b+a: return -1
            return 1

        str_list.sort(key=functools.cmp_to_key(comparator))
        if (str_list[0] == "0"):
            return "0"
        else: return "".join(str_list)
