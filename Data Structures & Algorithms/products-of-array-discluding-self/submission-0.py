class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = nums[:]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i] * right[i+1]
        
        lef = 1
        res = []
        for i in range(len(nums) - 1):
            res.append(lef*right[i+1])
            lef*=nums[i]
        res.append(lef)
        return res