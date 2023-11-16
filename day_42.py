from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                      
            if cur_sum > target: 
                return                  
            
            if cur_sum == target: 
                ans.append(cur) 
                return
            
            for i in range(idx, n): 
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i)

        dfs([], 0, 0)
        return ans    

if __name__ == "__main__":
    # Test cases
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
    print(solution.combinationSum([2, 3, 5], 8))   # Output: [[2, 2, 2, 2], [2, 3, 3], [5, 3]]
    print(solution.combinationSum([2], 1))         # Output: []
