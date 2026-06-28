class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0] * (len(nums) + 1)

        for i in range(1, len(pref)):
            pref[i] = pref[i-1] + nums[i-1]

        # piv

        for i in range(1, len(pref)):
            if pref[i-1] == pref[-1]- pref[i]:
                return i-1

        return - 1