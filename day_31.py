from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Define sets to keep track of seen numbers in rows, columns, and 3x3 boxes
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                # Check for rows
                if num in row_sets[i]:
                    return False
                row_sets[i].add(num)

                # Check for columns
                if num in col_sets[j]:
                    return False
                col_sets[j].add(num)

                # Check for 3x3 boxes
                box_index = (i // 3) * 3 + (j // 3)
                if num in box_sets[box_index]:
                    return False
                box_sets[box_index].add(num)

        return True

if __name__ == "__main__":
    # Example 1
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    print(sol.isValidSudoku(board1))  # Expected output: True

    # Example 2
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print(sol.isValidSudoku(board2))  # Expected output: False