class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        postfix = sum(nums)
        for i, num in enumerate(nums):
            postfix -= num
            if prefix == postfix:
                return i
            prefix += num

        return - 1