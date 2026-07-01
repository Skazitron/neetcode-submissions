class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def findSums(cur, idx, arr):
            if cur > target:
                return
            elif cur == target:
                ret.append(arr)
            else:
                for i in range(idx, len(nums)):
                    num = nums[i]
                    if cur + num <= target:
                        temp = arr[:]
                        temp.append(num)
                        findSums(cur + num, i, temp)

        findSums(0, 0, [])
        return ret