from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        # Calculate prefix sums from left to right
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        # Calculate suffix sums from right to left
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        # Calculate absolute differences
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
        return answer

if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    print(solution.leftRightDifference([10, 4, 8, 3]))  # Output: [15, 1, 11, 22]
    print(solution.leftRightDifference([1]))  # Output: [0]
