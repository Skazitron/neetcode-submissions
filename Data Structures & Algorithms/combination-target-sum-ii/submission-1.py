class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        
        def backtrack(idx, current_sum, path):
            if current_sum == target:
                ret.append(path[:]) 
                return
            if current_sum > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                if current_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
                
        backtrack(0, 0, [])
        return ret