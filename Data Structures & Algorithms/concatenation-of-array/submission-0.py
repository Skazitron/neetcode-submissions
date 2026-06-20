class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rar = []
        rar2 = []

        for i in range(len(nums)):
            rar.append(nums[i])
            rar2.append(nums[i])

        rar.extend(rar2)
        return rar