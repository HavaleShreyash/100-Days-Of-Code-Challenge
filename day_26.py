from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
        
if __name__ == "__main__":
    # Example usage:
    nums = [1, 2, 1]
    solution = Solution()
    print(solution.getConcatenation(nums))
