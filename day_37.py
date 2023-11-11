from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Make a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the element at the start position
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations for the remaining elements
                backtrack(start + 1)
                
                # Undo the swap for backtracking
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
    
if __name__ == "__main__":
    # Example usage:
    nums1 = [1, 2, 3]
    nums2 = [0, 1]
    nums3 = [1]

    solution = Solution()
    print(solution.permute(nums1))
    print(solution.permute(nums2))
    print(solution.permute(nums3))
