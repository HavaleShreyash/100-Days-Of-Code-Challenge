from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = [max(row) for row in grid]
        max_col = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total_increase = 0

        for i in range(n):
            for j in range(n):
                total_increase += min(max_row[i], max_col[j]) - grid[i][j]

        return total_increase

if __name__ == "__main__":
    # Example usage:
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    solution = Solution()
    print(solution.maxIncreaseKeepingSkyline(grid))