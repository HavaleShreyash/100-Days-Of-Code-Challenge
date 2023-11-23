import sys
def isValidSudoku(board):
    def is_valid_set(nums):
        seen = set()
        for num in nums:
            if num!='.':
                if num in seen:
                    return False
                seen.add(num)
        return True


    for row in board:
        if not is_valid_set(row):
            return False


    for col in zip(*board):
        if not is_valid_set(col):
            return False


    for i in range(0,9,3):
        for j in range(0,9,3):
            sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_set(sub_box):
                return False
    return True

def is_valid_sudoku_string(board_str):
    board_list = [list(row) for row in board_str.split()]
    return isValidSudoku(board_list)

def get_user_input():
    input_line = input()
    input_list = [input_line[i:i+9] for i in range(0, len(input_line), 9)]
    return [list(row) for row in input_list]


if __name__ == "__main__":
    user_sudoku_board = get_user_input()
    result = is_valid_sudoku_string(" ".join(["".join(row) for row in user_sudoku_board]))

    if result:
        print("Yes")
    else:
        print("No")